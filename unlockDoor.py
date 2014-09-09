#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO

doorUnlockPin=1
# board pin numbers are easier for me. If I move to another RPI version though... check the number
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(True)
GPIO.setup(doorUnlockPin,GPIO.OUT, pull_up_down = GPIO.PUD_UP) 

GPIO.output(doorUnlockPin,GPIO.LOW)
sleep (.5)
GPIO.output(doorUnlockPin,GPIO.HIGH)
GPIO.cleanup()