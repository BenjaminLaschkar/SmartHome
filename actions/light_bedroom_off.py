"""
This program turn off bedroom light.

The led of the bedroom is 13 on GPIO.
"""
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO_LAMPE = 13
GPIO.setup(GPIO_LAMPE, GPIO.OUT)
GPIO.output(GPIO_LAMPE, False)
