import socket
import ssl
import regex as rx

valid_url = False

try:
    url = input('Enter the url: ')
    url = rx.findall('//.*', url)[0][2 :] #removes http:// or https://

    url_host = rx.findall(".*?/", url)[0][0:-1] # if the url doesn't have http://, this throws an exception
    url_rest = rx.findall('/.*', url)[0]
    valid_url = True
except:
    print("Invalid url")

browser = "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0\r\n" + "Accept-Language: en-GB,en;q=0.5\r\n\r\n"  
package = "GET " + url_rest + " HTTP/1.1\r\n" + "Host: " + url_host + "\r\n" + "Connection: close\r\n" + browser

mysock_ssl = None

numchars = 0

def tryConnect():

    global numchars
    global mysock_ssl
    if(valid_url):
        mycontext_ssl = ssl.create_default_context()
        mysock_ssl = mycontext_ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),server_hostname=url_host)
        mysock_ssl.connect((url_host, 443))

    # print("CERTIFICATE:\n", mysock_ssl.getpeercert(), '\n\n')
    # print("VERSION:\n", mysock_ssl.version(), "\n\n")
        headers_ended = False
        
        mysock_ssl.send(package.encode())
        while numchars < 1700:
            data = mysock_ssl.recv(512)
            if len(data) < 1:
                break
            
            chunk_str = data.decode()
            if(rx.search('\r\n\r\n', chunk_str)): #gets approximate start of body
                headers_ended = True
            
            if(headers_ended):
                print(chunk_str[0 : (1700 - numchars)],end='')
            
                numchars = min(1700, numchars + len(chunk_str))

        mysock_ssl.close()

try:
    tryConnect()
    print(f'\nThe number of characters is {numchars}')
except:
    print("Error: connection failed, check the url")

try:
    mysock_ssl.close() 
except:
    print('no socket to close')

print('Done')

