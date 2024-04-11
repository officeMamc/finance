from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hi():
    return render_template("index.html")

@app.route("/create-account")
def crt_act():
    pass

@app.route("/search") 
def search():
    list = ["Vrushab", 'VCH', "KCH", "NCH"]
    query = request.args.get("q")
    if query in list:
        return render_template("search.html", query=query)
    return render_template("search.html")

@app.route("/search-resolve") 
def search_resolve():
    list = ["Vrushab", 'VCH', "KCH", "NCH"]
    query = request.args.get("q")
    if query in list:
        return query
    else:
        return "0"




app.run(host="0.0.0.0", port=5000, debug=True)