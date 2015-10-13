from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume')
def resume():
    return render_template('resume.html')


@app.route('/design')
def design():
    return render_template('design.html')


@app.route('/cryptomeria')
def cryptomeria():
    return render_template('cryptomeria.html')


@app.route('/oneclock')
def oneclock():
    return render_template('oneclock.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
