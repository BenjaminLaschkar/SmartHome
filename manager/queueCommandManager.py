"""
The queue command manager is the manager for control of the smart home.

It use a server to receive post request.
"""
from flask import Flask, render_template, request
from setting.configProxy import getIp, getPortQueueCommandManager
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
    command = command.replace(" ", "")
    return render_template('form_action.html', command=command)


# Run the app :)
if __name__ == '__main__':
    app.run(
        host=getIp(),
        port=getPortQueueCommandManager()
    )
