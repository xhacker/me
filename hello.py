from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cryptomeria')
def cryptomeria():
    return render_template('cryptomeria.html')

if __name__ == '__main__':
    app.run(debug=True)