import socket
import sys
from thread import *
import pyglet
        
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
            winsound.PlaySound('C:\Users\Public\Music\doorbell1.wav',winsound.SND_FILENAME)
        except msg:
            win32evtlogutil.ReportEvent(logType, 2,strings=['Ring failed Error Code : ' + str(msg[0]) + ' Message ' + msg[1],"ERROR DOORBELL"],
                                    data = "Raw\0Data".encode("ascii"))
        
        #start new thread
        start_new_thread(clientthread ,(conn,))
    
    s.close()
x = DoorBellService()