import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(20,GPIO.IN)
GPIO.setup(15,GPIO.OUT)
GPIO.setup(19,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(29,GPIO.OUT)
GPIO.setup(31,GPIO.OUT)
GPIO.setup(33,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT)


import csv

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)


if reader[0] == 1:               #1
   GPIO.output(15,GPIO.HIGH)
elif reader[0] == 0:
   GPIO.output(15,GPIO.ROW)

if reader[1] == 1:               #2
   GPIO.output(19,GPIO.HIGH)
elif reader[1] == 0:
   GPIO.output(19,GPIO.ROW)

if reader[2] == 1:               #3
   GPIO.output(21,GPIO.HIGH)
elif reader[2] == 0:
   GPIO.output(21,GPIO.ROW)

if reader[3] == 1:               #4
   GPIO.output(23,GPIO.HIGH)
elif reader[3] == 0:
   GPIO.output(23,GPIO.ROW)

if reader[4] == 1:               #5
   GPIO.output(27,GPIO.HIGH)
elif reader[4] == 0:
   GPIO.output(27,GPIO.ROW)

if reader[5] == 1:               #6
   GPIO.output(29,GPIO.HIGH)
elif reader[5] == 0:
   GPIO.output(29,GPIO.ROW)

if reader[6] == 1:               #7
   GPIO.output(31,GPIO.HIGH)
elif reader[6] == 0:
   GPIO.output(31,GPIO.ROW)

if reader[7] == 1:               #8
   GPIO.output(33,GPIO.HIGH)
elif reader[7] == 0:
   GPIO.output(33,GPIO.ROW)

if reader[8] == 1:               #9
   GPIO.output(35,GPIO.HIGH)
elif reader[8] == 0:
   GPIO.output(35,GPIO.ROW)

if reader[9] == 1:               #10
   GPIO.output(37,GPIO.HIGH)
elif reader[9] == 0:
   GPIO.output(37,GPIO.ROW)

GPIO.cleanup()
