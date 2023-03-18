from flask import app, current_app, Flask, request
import os
import requests
import json 

app = Flask("Chess")
@app.route("/")
def index():
    return open("Pages/index.html").read()

@app.route("/games/<id>")
def games(id):
    return "Games"
@app.route("/newgame", methods=['POST'] )
def newgame():
    print("newgame")
    return json.dumps({"id": getNewGameId()} )
def getNewGameId():
    return "1234"#Todo