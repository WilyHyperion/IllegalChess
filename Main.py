from flask import app, current_app, Flask, request
import os
import flask
import json 
InUseId = []
GameMoves = {
}
app = Flask("Chess")
@app.route("/")
def index():
    return open("Pages/index.html").read()
@app.route("/game")
def game():
    return open("Pages/game.html").read()

@app.route("/games/<id>", methods = ['GET'])
def games(id):

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
    GameMoves[id] = []
    return json.dumps({"id": id} )
def getNewGameId():
    id = 0
    while id in InUseId:
        id += 1
    InUseId.append(id)
    return id
<<<<<<< HEAD
  
=======
def getNextMove(id):
    return "TODO"
>>>>>>> 0a3687454545490fe2954cb3b10970dab8075fd7
