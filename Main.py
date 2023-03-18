from flask import app, current_app, Flask, request
import os
import flask
import requests
import json 
InUseId = []
app = Flask("Chess")
@app.route("/")
def index():
    return open("Pages/index.html").read()
@app.route("/game")
def game():
    return open("Pages/game.html").read()

@app.route("/games/<id>")
def games(id):
    return "Games"
@app.route("/newgame", methods=['POST'] )
def newgame():
    print("newgame")
    return json.dumps({"id": getNewGameId()} )
def getNewGameId():
    id = 0
    while id in InUseId:
        id += 1
    InUseId.append(id)
    return id
  
