"""
The queue command manager is the manager for control of the smart home.

It use a server to receive post request.
"""
from flask import Flask, render_template, request
from setting.configProxy import getIp, getPort
# Initialize the Flask application
app = Flask(__name__)


# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    """Page for POST throught the site."""
    return render_template('form_submit.html')


# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is
# accepting: POST requests in this case
@app.route('/sendcommand/', methods=['POST'])
def sendcommand():
    """Principal page for POST manually."""
    command = request.form['command']
    if(command == "LIGHT_LIVING_ROOM_ON"):
        light_living_room_on()
    elif(command == "LIGHT_LIVING_ROOM_OFF"):
        light_living_room_off()
    return render_template('form_action.html', command=command)


def light_living_room_on():
    """Launch program to light on the living room."""
    exec(open("../actions/light_living_room_on.py").read())


def light_living_room_off():
    """Launch program to light on the living room."""
    exec(open("../actions/light_living_room_off.py").read())

# Run the app :)
if __name__ == '__main__':
    app.run(
        host=getIp(),
        port=getPort()
    )
