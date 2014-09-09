import socket
import sys
import subprocess
from thread import *


def DoorBellService():
    HOST = ''   # Symbolic name meaning all available interfaces
    PORT = 9999
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #print 'Socket created'
    
    try:
        s.bind((HOST, PORT))
    except socket.error , msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()
    
    #print 'Socket bind complete'
    
    s.listen(10)
    #print 'Socket now listening'
    
    #Function for handling connections
    def clientthread(conn):
        #Sending message to connected client
        #conn.send('Welcome to the server. Receving Data...\n') #send only takes string
    
        conn.close()
    
    #now keep talking with the client
    while 1:
        #wait to accept a connection
        conn, addr = s.accept()
        print 'Connected with ' + addr[0] + ':' + str(addr[1])
        try:
            subprocess.Popen(["aplay","-d 3000","/opt/doorbell/doorbell1.wav"])
        except msg:
            print('Ring failed Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
        
        #start new thread
        start_new_thread(clientthread ,(conn,))
    
    s.close()
x = DoorBellService()