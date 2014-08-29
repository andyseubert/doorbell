#!/usr/bin/python
from time import sleep
import RPi.GPIO as GPIO

doorUnlockPin=4

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(doorUnlockPin,GPIO.OUT, pull_up_down = GPIO.PUD_DOWN)

GPIO.output(doorUnlockPin,GPIO.HIGH)
sleep (.5)
GPIO.output(doorUnlockPin,GPIO.LOW)