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
    if(command == "LIGHT_BATHROOM_ON"):
        light_bathroom_on()
    elif(command == "LIGHT_BATHROOM_OFF"):
        light_bathroom_off()
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
    elif(command == "LIGHT_AUTOMATIC_START_BATHROOM"):
        light_automatic_bathroom()
    elif(command == "OPEN_KITCHEN_CURTAIN"):
        curtain_kitchen_open()
    elif(command == "CLOSE_KITCHEN_CURTAIN"):
        curtain_kitchen_close()
    elif(command == "OPEN_BEDROOM_CURTAIN"):
        curtain_kitchen_open()
    elif(command == "CLOSE_BEDROOM_CURTAIN"):
        curtain_kitchen_close()

    return render_template('form_action.html', command=command)


def light_bathroom_on():
    """Launch program to light on the bathroom."""
    exec(open("../actions/light_bathroom_on.py").read())


def light_bathroom_off():
    """Launch program to light off the bathroom."""
    exec(open("../actions/light_bathroom_off.py").read())


def light_bedroom_on():
    """Launch program to light on the bedroom."""
    exec(open("../actions/light_bedroom_on.py").read())


def light_bedroom_off():
    """Launch program to light off the bedroom."""
    os.system("sudo pkill -f \"bedroom\"")
    exec(open("../actions/light_bedroom_off.py").read())


def light_kitchen_on():
    """Launch program to light on the kitchen."""
    os.system("sudo pkill -f \"kitchen\"")
    exec(open("../actions/light_kitchen_on.py").read())


def light_kitchen_off():
    """Launch program to light off the kitchen."""
    os.system("sudo pkill -f \"kitchen\"")
    exec(open("../actions/light_kitchen_off.py").read())


def light_automatic_kitchen():
    """Launch program to manage automaticly the kitchen."""
    os.chdir("/home/pi/SmartHome/automatic_mode")
    os.system("python3 light_kitchen.py &")


def light_automatic_bedroom():
    """Launch program to manage automaticly the bedroom."""
    os.chdir("/home/pi/SmartHome/automatic_mode")
    os.system("python3 light_bedroom.py &")


def light_automatic_bathroom():
    """Launch program to manage automaticly the bathroom."""
    os.chdir("/home/pi/SmartHome/automatic_mode")
    os.system("python3 light_bathroom.py &")


def curtain_kitchen_open():
    """Launch program to open the kitchen's curtain."""
    os.chdir("/home/pi/SmartHome/actions")
    os.system("sudo python curtain_kitchen_open.py")


def curtain_kitchen_close():
    """Launch program to close the kitchen's curtain."""
    os.chdir("/home/pi/SmartHome/actions")
    os.system("sudo python curtain_kitchen_close.py")


def curtain_bedroom_open():
    """Launch program to open the bedroom's curtain."""
    os.chdir("/home/pi/SmartHome/actions")
    os.system("sudo python curtain_bedroom_open.py")


def curtain_bedroom_close():
    """Launch program to close the bedroom's curtain."""
    os.chdir("/home/pi/SmartHome/actions")
    os.system("sudo python curtain_bedroom_close.py")


# Run the app :)
if __name__ == '__main__':
    app.run(
        host=getIp(),
        port=getPort()
    )
