from flask import Flask
from markov import *
app = Flask(__name__)

@app.route('/')
def index():
    values = createSentence()
    return values
