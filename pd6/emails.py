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
    'FOREIGN KEY(fk_sender_add) REFERNCES Addresses(id), FOREIGN KEY(fk_sender_dom) REFERNCES Domains(id)' \
    'FOREIGN KEY(fk_receiver_add) REFERNCES Addresses(id), FOREIGN KEY(fk_receiver_dom) REFERNCES Domains(id),' \
    'FOREIGN KEY(fk_weekday) REFERENCES Weekday(id))')

    address_id = 1
    domain_id = 1
    weekday_id = 1
    






    conn.commit()#finish the program
    conn.close()