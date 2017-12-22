from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Type the right urls for the themes'

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/vigenere')
def vignere():
    return render_template('vigenere.html')


if __name__ == '__main__':
    app.run()
