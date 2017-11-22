"""
This program turn on bedroom light.

The led of the bedroom is 13 on GPIO.
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO_LAMPE = 13
GPIO.setup(GPIO_LAMPE, GPIO.OUT)
GPIO.output(GPIO_LAMPE, True)
