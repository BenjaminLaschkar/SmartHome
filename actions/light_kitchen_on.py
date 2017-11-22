"""
This program turn on kitchen light.

The led of the kitchen is 11 on GPIO.
"""
import RPi.GPIO as GPIO
import os
os.system("sudo pkill -f \"kitchen\"")
GPIO.setmode(GPIO.BCM)
GPIO_LAMPE = 6
GPIO.setup(GPIO_LAMPE, GPIO.OUT)
GPIO.output(GPIO_LAMPE, True)
