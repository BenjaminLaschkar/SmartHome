#!/usr/bin/python

from Adafruit_PWM_Servo_Driver import PWM
import time

# ===========================================================================
# Example Code
# ===========================================================================

# Initialise the PWM device using the default address
pwm = PWM(0x40)
# Note if you'd like more debug output you can instead run:
# pwm = PWM(0x40, debug=True)

servoMin = 100  # Min pulse length out of 4096
servoMax = 800  # Max pulse length out of 4096


def setServoPulse(channel, pulse):
    """Change pulse of servo."""
    pulseLength = 1000000                   # 1,000,000 us per second
    pulseLength /= 60                       # 60 Hz
    print "%d us per period" % pulseLength
    pulseLength /= 4096                     # 12 bits of resolution
    print "%d us per bit" % pulseLength
    pulse *= 1000
    pulse /= pulseLength
    pwm.setPWM(channel, 0, pulse)

while True:
    pwm.setPWMFreq(60)                        # Set frequency to 60 Hz
    pwm.setPWM(5, 5, servoMin)
    time.sleep(1)
    pwm.setPWM(5, 5, servoMax)
    time.sleep(1)
