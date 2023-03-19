from flask import app, current_app, Flask, request, send_from_directory
import os
import flask
import json 
import random
import Scrapper
#import cohere
promptStart = f"""
     play a game of chess with me. Respond only with what you move and what place it moved to
"""

InUseId = []
GameMoves = {
}
app = Flask("Chess")
@app.route("/games/img/<path:path>")
def img(path):
    print(path) 
    return send_from_directory("Pages/img", path)
@app.route("/")
def index():
    return open("Pages/index.html").read()
@app.route("/game")
def game():
    return open("Pages/game.html").read()
@app.route("/games/<id>/move", methods = ['POST'])
def move(id):
    id = int(id)
    if id not in InUseId:
        return "Invalid Game Id"
    GameMoves[id].append(request.json['move'])
    return getNextMove(id)
@app.route("/games/<id>", methods = ['GET'])
def games(id):
    id = int(id)
    if id not in InUseId:
        return "Invalid Game Id"
    return open("Pages/game.html").read()
@app.route("/games/<id>", methods = ['POST'])
def postGame(id):
    numid = int(id)
    GameMoves[numid].append(request.json['move'])
    n = getNextMove(id)
    GameMoves[numid].append(n)
    return json.dumps({"move": n}) 
@app.route("/newgame", methods=['POST'] )
def newgame():
    id = getNewGameId()
    print(InUseId)
    GameMoves[id] = []
    return json.dumps({"id": id} )
@app.route("/games/<id>/end", methods = ['GET'])
def endgame(id):
    id = int(id)
    if id not in InUseId:
        return "Invalid Game Id"
    InUseId.remove(id)
    del GameMoves[id]
    return "Game Ended"
def getNewGameId():
    id = random.randint(100, 999)
    while id in InUseId:
        id = random.randint(100, 999)
    InUseId.append(id)
    return id
def getNextMove(id, move):
    id = int(id)
    
    return "e5"