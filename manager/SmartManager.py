"""
The queue command manager is the manager for control of the smart home.

It use a server to receive post request.
"""
from flask import Flask, render_template, request
from setting.configProxy import getIp, getPort
import os
# Initialize the Flask application
app = Flask(__name__)


# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    """Page for POST throught the site."""
    return render_template('form_submit.html')


# POST requests in this case
@app.route('/sendcommand/', methods=['POST'])
def sendcommand():
    """Principal page for POST manually."""
    command = request.form['command']
    if(command == "LIGHT_LIVING_ROOM_ON"):
        light_living_room_on()
    elif(command == "LIGHT_LIVING_ROOM_OFF"):
        light_living_room_off()
    elif(command == "LIGHT_BEDROOM_ON"):
        light_bedroom_on()
    elif(command == "LIGHT_BEDROOM_OFF"):
        light_bedroom_off()
    elif(command == "LIGHT_KITCHEN_ON"):
        light_kitchen_on()
    elif(command == "LIGHT_KITCHEN_OFF"):
        light_kitchen_off()
    elif(command == "LIGHT_AUTOMATIC_START_KITCHEN"):
        light_automatic_kitchen()
    elif(command == "LIGHT_AUTOMATIC_START_BEDROOM"):
        light_automatic_bedroom()
    elif(command == "LIGHT_AUTOMATIC_START_LIVING_ROOM"):
        light_automatic_living_room()
    return render_template('form_action.html', command=command)


def light_living_room_on():
    """Launch program to light on the living room."""
    os.system("sudo pkill -f \"living_room\"")
    exec(open("../actions/light_living_room_on.py").read())


def light_living_room_off():
    """Launch program to light off the living room."""
    os.system("sudo pkill -f \"living_room\"")
    exec(open("../actions/light_living_room_off.py").read())


def light_bedroom_on():
    """Launch program to light on the bedroom."""
    os.system("sudo pkill -f \"bedroom\"")
    exec(open("../actions/light_bedroom_on.py").read())


def light_bedroom_off():
    """Launch program to light off the bedroom."""
    os.system("sudo pkill -f \"bedroom\"")
    exec(open("../actions/light_bedroom_off.py").read())


def light_kitchen_on():
    """Launch program to light on the kitchen."""
    os.system("sudo pkill -f \"light_kitchen\"")
    exec(open("../actions/light_kitchen_on.py").read())


def light_kitchen_off():
    """Launch program to light off the kitchen."""
    os.system("sudo pkill -f \"light_kitchen\"")
    exec(open("../actions/light_kitchen_off.py").read())


def light_automatic_kitchen():
    """Launch program to manage automaticly the kitchen."""
    os.chdir("/home/pi/SmartHome/automatic_mode")
    os.system("python3 light_kitchen.py &")


def light_automatic_bedroom():
    """Launch program to manage automaticly the bedroom."""
    os.chdir("/home/pi/SmartHome/automatic_mode")
    os.system("python3 light_bedroom.py &")


def light_automatic_living_room():
    """Launch program to manage automaticly the living_room."""
    os.chdir("/home/pi/SmartHome/automatic_mode")
    os.system("python3 light_living_room.py &")


# Run the app :)
if __name__ == '__main__':
    app.run(
        host=getIp(),
        port=getPort()
    )
