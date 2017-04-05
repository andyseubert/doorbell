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



print ("READY")

# 04/05/2017 - removed "event_detect" code and switched to "wait_for_edge" 
# in an attempt to remove spurious button presses.
# the code does NOTHING else, so I figured I'd give it a try.
# I didn't realize there was a bouncetime paramater at first 
# and adding that definitely stopped the bouncing.

while (True):
    GPIO.wait_for_edge(bellButtonPin,GPIO.FALLING,bouncetime=200)
## read the list of hosts listening from a configuration file
    with open('/opt/doorbell/listeners.txt') as f:
        listeners = f.read().splitlines()
    for host in listeners:
        print "ringing " + host
        subprocess.Popen([sys.executable, alertcmd, host])

#subprocess.Popen([sys.executable,"/opt/doorbell/unlockDoor.py"])
    subprocess.Popen([sys.executable,"/opt/doorbell/sendsms.py","DingDong"])


	
GPIO.cleanup()
