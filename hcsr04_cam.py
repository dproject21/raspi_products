#!/usr/bin/env python
# -*- coding : utf-8 -*-

def reading(sensor):
    import time
    import RPi.GPIO as GPIO
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BOARD)
    TRIG = 3
    ECHO = 5
    LCD = 11

    if sensor == 0:
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)
        GPIO.setup(LCD, GPIO.OUT)
        GPIO.output(TRIG, GPIO.LOW)
        time.sleep(0.3)

        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            signaloff = time.time()

        while GPIO.input(ECHO) == 1:
            signalon = time.time()

        timepassed = signalon - signaloff
        distance = timepassed * 17000

        if distance < 50:
            GPIO.output(LCD, True)
        else:
            GPIO.output(LCD, False)
        
        return distance
        GPIO.cleanup()
    else:
        print "Incorrect usonic() function variable."

import subprocess
count = 0

for i in range(50):
    result = reading(0)
    print result
    if result < 50:
        count += 1
    else:
        count = 0

    if count == 4:
        cmd = "fswebcam /home/pi/tmp.jpg"
        subprocess.call(cmd.strip().split(" "))
        count = 0
