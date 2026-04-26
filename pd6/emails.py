import regex as rx
from pathlib import Path
import requests
import sqlite3

base = Path(__file__).resolve().parent
git_base = Path(__file__).parent

handle_mbox = None
handle_db = None
try:
    handle_mbox = open(base/'mbox-short.txt', 'r')
    handle_db = open(base/'emails.sqlite', 'r')
except:
    handle_mbox = requests.get('https://raw.githubusercontent.com/Neondertalec/PythonTeam8/main/pd6/mbox-short.txt').text
    handle_db = requests.get('https://raw.githubusercontent.com/Neondertalec/PythonTeam8/main/pd6/emails.sqlite').text

if (handle_db != None and handle_mbox != None) :
    conn = sqlite3.connect(handle_db)
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS Addresses')
    cur.execute('CREATE TABLE Addresses (id INTEGER PRIMARY KEY, email_address TEXT)')
    cur.execute('DROP TABLE IF EXISTS Domains')
    cur.execute('CREATE TABLE Domains (id INTEGER PRIMARY KEY, domain_address TEXT)')
    cur.execute('DROP TABLE IF EXISTS Weekdays')
    cur.execute('CREATE TABLE Weekdays (id INTEGER PRIMARY KEY, day TEXT)')
    cur.execute('DROP TABLE IF EXISTS Emails')
    cur.execute('CREATE TABLE Emails (id INTEGER PRIMARY KEY, ' \
    'fk_sender_add INTEGER, fk_sender_dom INTEGER, fk_receiver_add INTEGER, fk_receiver_dom INTEGER, ' \
    'fk_weekday INTEGER, spam_prob REAL,' \
    'FOREIGN KEY(fk_sender_add) REFERENCES Addresses(id), FOREIGN KEY(fk_sender_dom) REFERENCES Domains(id)' \
    'FOREIGN KEY(fk_receiver_add) REFERENCES Addresses(id), FOREIGN KEY(fk_receiver_dom) REFERENCES Domains(id),' \
    'FOREIGN KEY(fk_weekday) REFERENCES Weekday(id))')

    send_address_id = 1
    send_domain_id = 1
    rec_address_id = 1
    rec_domain_id = 1
    fk_weekday_id = 1
    address_id = 1
    domain_id = 1
    weekday_id = 1
    
    # --PARSE--
    for line in handle_mbox.splitlines():
        try_address = rx.findall('From: .*', line)
        is_sender = False
        if len(try_address) > 0:
            is_sender = True
            try_address[0] = try_address[0][2 : ] # equalizes length to address lines that start with 'To: '
        else:
            try_address = rx.findall('To: .*', line)
        
        if len(try_address) > 0:
            try_address[0] = try_address[0][4 : ]

            address_portion = rx.findall('.*@', try_address[0])[0][ : -1]
            domain_portion = rx.findall('@.*', try_address[0])[0][1 : ]

            cur.execute('SELECT id FROM Addresses WHERE email_address = ?', (address_portion,))
            result = cur.fetchone()
            if result:
                fk_address_id = result[0]
            else:
                cur.execute('INSERT INTO Addresses (id, email_address) VALUES (?, ?)', (address_id, address_portion))
                fk_address_id = address_id
                address_id += 1
            
            cur.execute('SELECT id FROM Domains WHERE domain_address = ?', (domain_portion,))
            result = cur.fetchone()
            if result:
                fk_domain_id = result[0]
            else:
                cur.execute('INSERT INTO Domains (id, domain_address) VALUES (?, ?)', (domain_id, domain_portion))
                fk_domain_id = domain_id
                domain_id += 1
            
            if(is_sender):
                send_address_id = fk_address_id
                send_domain_id = fk_domain_id
            else:
                rec_address_id = fk_address_id
                rec_domain_id = fk_domain_id
        
        try_date = rx.findall('Date: [a-zA-Z]*?,', line)
        if len(try_date) > 0:
            weekday = try_date[0][6 : -1]
            cur.execute('SELECT id FROM Weekdays WHERE day = ?', (weekday,))
            result = cur.fetchone()
            if result:
                fk_weekday_id = result[0]
            else:
                cur.execute('INSERT INTO Weekdays (id, day) VALUES (?, ?)', (weekday_id, weekday))
                fk_weekday_id = weekday_id
                weekday_id += 1
        
        try_spam_rating = rx.findall('X-DSPAM-Confidence: .*', line)

        if len(try_spam_rating) > 0:
            probability = float(try_spam_rating[0][20 : ])

            cur.execute('INSERT INTO Emails (fk_sender_add , fk_sender_dom , fk_receiver_add, fk_receiver_dom, ' \
                'fk_weekday, spam_prob) VALUES (?, ?, ?, ?, ?, ?)',
                (send_address_id, send_domain_id, rec_address_id, rec_domain_id, fk_weekday_id, probability))

    # --END_PARSE--

    #parser test
    cur.execute('SELECT spam_prob, email_address FROM Emails LEFT JOIN Addresses ON Addresses.id = fk_sender_add') 
    for row in cur:
        print(row)



    conn.commit()#finish the program
    conn.close()