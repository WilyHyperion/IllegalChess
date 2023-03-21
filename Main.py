from flask import app, current_app, Flask, request, send_from_directory
import os
import flask
import json
import random
import re
# import Scrapper
import GPTScrapper

#Default prompt
#promptStart = f"""Let's play a game of Chess. I will be white you will be black. You will respond with a single move, in standard chess notation. You will not include any other comments, just the single move. You are a player that plays extremely offensively and likes to capture pieces whenever possible. If you think an move is illegal or invalid, still provide a move. Moves:"""

# All pieces are Knights prompt
promptStart = f"""Let's play a game of Chess. I will be white you will be black. You will respond with a single move, in standard chess notation. You will not include any other comments, just the single move. We are playing a variation of chess called "Knight chess". In pawn chess, all of black's pieces except for the king is a knight. If you think an move is illegal or invalid, still provide a move. Moves:"""

InUseId = []
GameMoves = {

}

app = Flask("Chess")

counter = 0


@app.route("/favicon.ico")
def imag():
    return send_from_directory("Pages/img/anarchy.png", "anarchy.png")


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


@app.route("/games/<id>/move", methods=['POST'])
def move(id):
    id = int(id)
    if id not in InUseId:
        return open("Pages/invalid.html").read()
    GameMoves[id].append(request.json['move'])
    return getNextMove(id)


@app.route("/games/<id>", methods=['GET'])
def games(id):
    id = int(id)
    if id not in InUseId:
        return open("Pages/invalid.html").read()
    return open("Pages/game.html").read()


@app.route("/games/<id>", methods=['POST'])
def postGame(id):
    numid = int(id)
    GameMoves[numid].append(request.json['move'])
    n = getNextMove(id)
    GameMoves[numid].append(n)
    return json.dumps({"move": n})


@app.route("/newgame", methods=['POST'])
def newgame():
    id = getNewGameId()
    print(InUseId)
    GameMoves[id] = []
    return json.dumps({"id": id})


@app.route("/games/<id>/end", methods=['GET'])
def endgame(id):
    id = int(id)
    if id not in InUseId:
        return open("Pages/invalid.html").read()
    InUseId.remove(id)
    del GameMoves[id]
    return "Game Ended"


def getNewGameId():
    id = random.randint(100, 999)
    while id in InUseId:
        id = random.randint(100, 999)
    InUseId.append(id)
    return id


def getNextMove(id, special=False):
    id = int(id)
    moves = GameMoves[id]
    p = promptStart;
    if len(moves) > 1:
        if counter % 3 == 1:
            p = f"""I make the move {moves[-1]}. Here are the previous moves: {moves}. Provide your response in standard 
        chess notation with no accompanying text."""
        else:
            p = f"""I make the move {moves[-1]}."""
    else:
        for i in moves:
            p += i + " "
    print(p)
    s = GPTScrapper.gettext(p)
    print(s)

    # split s by spaces and find the first one that is a valid move. find a valid move by seeing if there is a number
    # and a letter in the text anywhere
    if " " in s or "." in s:
        while " " in s or "." in s:
            s = GPTScrapper.gettext(
                "I will give you text, please parse it to find the move. Respond with only that move, no" 
                "other accompanying comments. Here is the text: \"" + s + "\". If there is no chess move, create a random chess move.")
            #for some reason "noother" gives a better parsed text than "no other"

            print(s + "[replaced]")
        """ move = s.split(" 0")
      hasInt = False;
      hasStr = False;
      for i in move:
        for j in i:
          if j.isnumeric():
            hasInt = True
          if j.isalpha():
            hasStr = True
        if(hasInt and hasStr):
          s = move.index(i)
        else:
          hasInt = False
          hasStr = False
      if(s == temp):
        s = "e4" """
    moves.append(s)
    if "+" in s:
        s.replace("+", "")
    if "#" in s:
        s.replace("#", "")
    if "x" in s:
        # if there is an x, remove it
        s.replace("x", "")
    return s.lower()


@app.route("/games/<id>/comments", methods=['GET'])
def getComments(id):
    id = int(id)
    if id not in InUseId:
        return "bad game id"
    return GPTScrapper.getUnRealtedText(
        "Provide a comment on the chess game, with these moves. Make your comments helpful for someone trying to learn chess while also being less than 30 words: " + str(
            GameMoves[id]))
