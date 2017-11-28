"""
This program manage the light in the kitchen.

The led of the kitchen is 11 on GPIO.
"""
import RPi.GPIO as GPIO
import time
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)
# set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 4
GPIO_LAMPE = 6
# set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)
GPIO.setup(GPIO_LAMPE, GPIO.OUT)


def distance():
    """Compute the distance."""
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)
    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)
    StartTime = time.time()
    StopTime = time.time()
    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()
    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()
    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2
    return distance


if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
            if(dist < 20):
                GPIO.output(GPIO_LAMPE, True)
            else:
                GPIO.output(GPIO_LAMPE, False)
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        # print("Measurement stopped by User")
        GPIO.cleanup()
