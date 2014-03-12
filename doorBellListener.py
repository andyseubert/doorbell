#!/usr/bin/python
from time import sleep
import os
import sys
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO

# global variables for commands and status
global alertcmd
alertcmd = "./ringer.py" 
## read the list of hosts listening from a configuration file
with open('./listeners.txt') as f:
    listeners = f.read().splitlines()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(2, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # Front push button 

def alert_action(channel):
	from time import sleep	
	print('Edge detected on channel %s'%channel)
	for host in listeners:
		subprocess.Popen([sys.executable, alertcmd, host])
print ("READY")

GPIO.add_event_detect(2, GPIO.FALLING, callback=alert_action, bouncetime=200) 

while True:
	sleep(1)
	
GPIO.cleanup()