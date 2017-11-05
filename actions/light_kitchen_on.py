"""
This program turn on kitchen light.

The led of the kitchen is 11 on GPIO.
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO_LAMPE = 11
GPIO.setup(GPIO_LAMPE, GPIO.OUT)
GPIO.output(GPIO_LAMPE, True)
