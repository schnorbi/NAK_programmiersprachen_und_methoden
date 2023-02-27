from flask import Flask
import RPi.GPIO as GPIO

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello still running!"

@app.route("/gpio/<pin>/on")
def on_gpio(pin):
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (int(pin), GPIO.OUT)

    GPIO.output(int(pin), False)

    return f"{pin} wurde auf True gesetzt"

@app.route("/gpio/<pin>/off")
def off_gpio(pin):
    GPIO.setmode (GPIO.BOARD)
    GPIO.setup (int(pin), GPIO.OUT)

    GPIO.output(int(pin), True)

    return f"{pin} wurde auf False gesetzt"

app.run(host="0.0.0.0")