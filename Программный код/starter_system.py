import RPi.GPIO as GPIO
import os
import time as t

KEY = 4

GPIO.setmode(GPIO.BCM)

GPIO.setup(KEY, GPIO.IN)

while True:
    if GPIO.input (KEY) == False:
        os.system("python3 /home/pi/Desktop/Voise_mode_for_rasberry.py")
    else:
        print("0")
        t.sleep(1)
