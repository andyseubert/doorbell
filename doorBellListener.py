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


# adding debounce code found here:
# http://raspberrypi.stackexchange.com/a/50530
def debouncedInput(pin):
    tries = 12
    i, ones, zeroes = 0, 0, 0
    while i < tries:
        bit=GPIO.input(pin)
        if (bit == 1):
           ones = ones + 1
           zeroes = 0
        else:
           zeroes = zeroes + 1
           ones = 0
        i = i + 1
	### return 1 for zeroes if a button grounds when pushed
	### return 1 for ones if a button goes positive when pushed
        if (ones >= 3):
            return 0
        if (zeroes >=3):
            return 1
        time.sleep(0.5) # wait a bit

    # indeterminate state, tries exhausted
    logging.error ('Bouncy input: %s', pin) 
    return (bit)   #best effort 

def alert_action(channel):
	if (debouncedInput(bellButtonPin)):
		from time import sleep	
		## read the list of hosts listening from a configuration file
		with open('/opt/doorbell/listeners.txt') as f:
			listeners = f.read().splitlines()
		print('Edge detected on channel %s'%channel)
		for host in listeners:
			print "ringing " + host
			subprocess.Popen([sys.executable, alertcmd, host])

		# subprocess.Popen([sys.executable,"/opt/doorbell/unlockDoor.py"])
		#	subprocess.Popen([sys.executable,"/opt/doorbell/sendsms.py","DingDong"])
		#sleep (1)
print ("READY")

GPIO.add_event_detect(bellButtonPin, GPIO.FALLING, callback=alert_action, bouncetime=500) 

while True:
	sleep(1)
	
GPIO.cleanup()
