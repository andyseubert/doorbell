#!/usr/bin/python
from time import sleep
import os
import sys
import subprocess
from subprocess import Popen
import RPi.GPIO as GPIO
import time


# global variables for commands and status
global alertcmd
alertcmd = "/opt/doorbell/ringer.py" 

bellButtonPin=26
# board pin numbers are easier for me. If I move to another RPI version though... check the number
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(bellButtonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)  # Front push button 


# adding code found here:
# http://raspberrypi.stackexchange.com/a/50530
# this is not so much debouncing, rather avoiding spurious signals
# the thinking is that the "debouncedInput" code checks to make sure the 
# pin is signaled for more than a few milliseconds....
# I am not sure it's working. In fact I rather suspect it is not working
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
        if (ones >= 3):
            return 1
        if (zeroes >=3):
            return 0
        time.sleep(0.5) # wait a bit

    # indeterminate state, tries exhausted
    logging.error ('Bouncy input: %s', pin) 
    return (bit)   #best effort 

print ("READY")

#def alert_action(channel):
# 04/05/2017 - removed "event_detect" code and switched to "wait_for_edge" 
# in an attempt to remove spurious button presses.
# the code does NOTHING else, so I figured I'd give it a try.
# I didn't realize there was a bouncetime paramater at first 
# and adding that definitely stopped the bouncing.

while (True):
 GPIO.wait_for_edge(bellButtonPin,GPIO.FALLING,bouncetime=500)
#  if (debouncedInput(bellButtonPin)):
 time.sleep(0.1)         # need to filter out the false positive of some power fluctuation
 if GPIO.input(bellButtonPin) != GPIO.HIGH:
   print("spurious signal")
 else:
   #    from time import sleep	
   ## read the list of hosts listening from a configuration file
   with open('/opt/doorbell/listeners.txt') as f:
     listeners = f.read().splitlines()
   for host in listeners:
     print "ringing " + host
     subprocess.Popen([sys.executable, alertcmd, host])

   #subprocess.Popen([sys.executable,"/opt/doorbell/unlockDoor.py"])
   subprocess.Popen([sys.executable,"/opt/doorbell/sendsms.py","DingDong"])


	
GPIO.cleanup()
