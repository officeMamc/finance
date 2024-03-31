from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hi():
    return render_template("index.html")

@app.route("/create-account")
def crt_act():
    pass

app.run(host="0.0.0.0", port=5000, debug=True)