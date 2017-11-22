"""
This program turn on living room light.

The led of the living room is 7 on GPIO.
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO_LAMPE = 25
GPIO.setup(GPIO_LAMPE, GPIO.OUT)
GPIO.output(GPIO_LAMPE, True)
