#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO

doorUnlockPin=5
# board pin numbers are easier for me. If I move to another RPI version though... check the number
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(doorUnlockPin,GPIO.OUT, pull_up_down = GPIO.PUD_UP) 

GPIO.output(doorUnlockPin,GPIO.HIGH)
sleep (.5)
GPIO.output(doorUnlockPin,GPIO.LOW)