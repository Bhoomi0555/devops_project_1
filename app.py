from flask import Flask

app = Flask(__name__)

@app.route("/info")
def lwinfo():
        return "I am LW"

@app.route("/phone")
def lwphone():
        return "8875097255"

app.run(host="0.0.0.0")
