#!/usr/bin/python
import socket   
import sys  
import struct
import time

debug=1
#main function
if __name__ == "__main__":

    if(len(sys.argv) < 2) :
        print 'Usage : python client.py hostname'
        sys.exit()

    host = sys.argv[1]
    port = 9999

#create an INET, STREAMing socket
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(3)
except socket.error:
    print 'Failed to create socket'
    sys.exit()

#print 'local Socket Created'

try:
    print 'ringing : ' + host
    remote_ip = socket.gethostbyname( host )
    s.connect((host, port))

except socket.gaierror:
    print 'Hostname could not be resolved. Exiting'
    sys.exit()

except socket.error:
    if debug: print "could not contact " + host
    sys.exit()
    
#print 'Socket Connected to ' + host + ' on ip ' + remote_ip
s.settimeout(None)
#Send some data to remote server
# make it like a "PSK" kind of thing
message = "Q60NQzca32NU8zUuEOSPHmnnXKsSJNereT71yBNcgSAxj4TYqeAxOQAXnWn1jXs"
#message = "Q6NQzca32NU8zUuEOSPHmnnXKsSJNereT71yBNcgSAxj4TYqeAxOQAXnWn1jXs"

try :
    s.send(message)
    if debug: print 'Key sent successfully'
    
except socket.error:
    #Send failed
    if debug: print 'receive failed'
    sys.exit()
    
data = s.recv(1024)
if debug: print data+"\n"

s.close()
