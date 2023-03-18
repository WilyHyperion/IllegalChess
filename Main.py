from flask import app, current_app, Flask, request
import os
import requests
requests.get("https://chat.openai.com/chat")
import cohere

app = flask.Flask("Chess")
@route("/")
def index():
    return open("Pages/index.html").read()
app.route("/games/")
def games():
    return "Games";