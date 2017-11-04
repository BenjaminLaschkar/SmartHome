"""
This program launch living room light.

The led of the living room is 7 on GPIO.
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO_LAMPE = 7
GPIO.setup(GPIO_LAMPE, GPIO.OUT)
GPIO.output(GPIO_LAMPE, False)
