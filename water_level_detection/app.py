#------------------------------------------------------------
# Imports
import time
from flask import *
import RPi.GPIO as GPIO
from datetime import datetime

#------------------------------------------------------------
# Setup
app = Flask(__name__)

TRIG = 16
ECHO = 18

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(TRIG, GPIO.OUT)
	GPIO.setup(ECHO, GPIO.IN)

def distance():
	GPIO.output(TRIG, 0)
	time.sleep(0.000002)

	GPIO.output(TRIG, 1)
	time.sleep(0.00001)
	GPIO.output(TRIG, 0)


	while GPIO.input(ECHO) == 0:
		a = 0
	time1 = time.time()
	while GPIO.input(ECHO) == 1:
		a = 1
	time2 = time.time()

	during = time2 - time1
	return during * 340 / 2 * 100


#------------------------------------------------------------
# Flask

@app.route('/')
def index():
    setup()
    dis = distance()
    percent = (dis-3)/.24


    blue_line = round(percent*2.6)
    gray_line = 260-blue_line


    return render_template('index.html', blue_line=blue_line, gray_line=gray_line)
    
if __name__ == '__main__':
    app.run(debug=True, port=80, host='0.0.0.0') 
