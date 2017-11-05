"""
This program manage the light in the living room.

The led of the kitchen is 11 on GPIO.
"""
import RPi.GPIO as GPIO
import sys
import time
from daemon import Daemon

# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
# set GPIO Pins
GPIO_TRIGGER = 12
GPIO_ECHO = 18
GPIO_LAMPE = 11
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


class YourCode(object):
    def run(self):
        while True:
            dist = distance()
            # print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.3)
            if(dist < 20):
                GPIO.output(GPIO_LAMPE, True)
            else:
                GPIO.output(GPIO_LAMPE, False)


class MyDaemon(Daemon):
    def run(self):
        # Or simply merge your code with MyDaemon.
        your_code = YourCode()
        your_code.run()


if __name__ == "__main__":
    daemon = MyDaemon('/tmp/daemon-example.pid')
    if len(sys.argv) == 2:
        if 'start' == sys.argv[1]:
            daemon.start()
        elif 'stop' == sys.argv[1]:
            daemon.stop()
        elif 'restart' == sys.argv[1]:
            daemon.restart()
        else:
            print "Unknown command"
            sys.exit(2)
        sys.exit(0)
    else:
        print "usage: %s start|stop|restart" % sys.argv[0]
        sys.exit(2)
