from flask import Flask, render_template
import RPi.GPIO as GPIO
import datetime
app = Flask(__name__)

@app.route("/")
def hello():
    try:
        if lightOn == True:
            lightOn = False
        else:
            lightOn = True
    except UnboundLocalError:
        lightOn = True

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(7, GPIO.OUT)
    GPIO.output(7,lightOn)

    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
    return render_template('main.html', **templateData)

if __name__ == "__main__":
   app.run(host='0.0.0.0', port=80, debug=True)
