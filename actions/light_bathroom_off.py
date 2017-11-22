"""
This program turn off bathroom light.

The led of the bathroom is 7 on GPIO.
"""
import RPi.GPIO as GPIO
import os
os.system("sudo pkill -f \"bathroom\"")
GPIO.setmode(GPIO.BCM)
GPIO_LAMPE = 25
GPIO.setup(GPIO_LAMPE, GPIO.OUT)
GPIO.output(GPIO_LAMPE, False)
