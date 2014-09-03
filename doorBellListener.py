#!/usr/bin/python
from time import sleep
import os
import sys
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO


# global variables for commands and status
global alertcmd
alertcmd = "/opt/doorbell/ringer.py" 

bellButtonPin=26
# board pin numbers are easier for me. If I move to another RPI version though... check the number
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(bellButtonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # Front push button 
def alert_action(channel):
	from time import sleep	
	## read the list of hosts listening from a configuration file
	with open('/opt/doorbell/listeners.txt') as f:
	    listeners = f.read().splitlines()
	print('Edge detected on channel %s'%channel)
	for host in listeners:
		print "ringing " + host
		subprocess.Popen([sys.executable, alertcmd, host])
		
	# subprocess.Popen([sys.executable,"/opt/doorbell/unlockDoor.py"])
	subprocess.Popen([sys.executable,"/opt/doorbell/sendsms.py","You Rang?"])
	#sleep (1)
print ("READY")

GPIO.add_event_detect(bellButtonPin, GPIO.FALLING, callback=alert_action, bouncetime=300) 

while True:
	sleep(1)
	
GPIO.cleanup()
