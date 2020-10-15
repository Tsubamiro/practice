import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(6,GPIO.IN)

x = 1

if x == 1:
    GPIO.output(21,GPIO.HIGH)