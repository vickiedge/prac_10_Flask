from flask import Flask

app = Flask(__name__)


@app.route('/')
def temperatures():
    return '<h1>Temperatures! Enter celsius value to convert to the end of the browser bar and press enter;)</h1>'

@app.route('/<celsius>')
def convert_temp (celsius=""):
    celsius_float = float(celsius)
    fahrenheit = celsius_float * 9.0 / 5 + 32
    return ("The celsius temp {:.2f} degrees C converted to fahrenheit is {:.2f} degrees F".format(celsius_float, fahrenheit))


if __name__ == '__main__':
    app.run()