"""
This program manage the light in the bathroom.

The led of the bathroom is 7 on GPIO.
"""
import RPi.GPIO as GPIO
import time
import sys
from urllib import request, parse
sys.path.append('/home/pi/SmartHome/manager/setting')
from configProxy import getIp, getPort


def send(value):
        data = parse.urlencode({"command": value}).encode()
        url = "http://" + str(getIp()) + ":" + str(getPort()) + "/sendcommand/"
        req = request.Request(url, data=data)
        resp = request.urlopen(req)


send("LIGHT_KITCHEN_ON")
