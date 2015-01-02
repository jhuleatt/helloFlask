from flask import Flask, render_template
import RPi.GPIO as GPIO
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
    return render_template('main.html', **templateData)

@app.route("/on")
def turnOn():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7,True)

    return "Light is on"

@app.route("/off")
def turnOff():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7,False)

    return "Light is off"

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
