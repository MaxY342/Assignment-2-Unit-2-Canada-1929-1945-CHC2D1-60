from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/exhibit1")
def exhibit1():
    return render_template("exhibit1.html")

@app.route("/exhibit2")
def exhibit2():
    return render_template("exhibit2.html")

@app.route("/exhibit3")
def exhibit3():
    return render_template("exhibit3.html")

@app.route("/exhibit4")
def exhibit4():
    return render_template("exhibit4.html")

@app.route("/backpage")
def backpage():
    return render_template("backpage.html")
