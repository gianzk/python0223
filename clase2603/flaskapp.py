from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/demo")
def demo():
    return "Hello, demo2!"

app.debug=True

app.run()