from flask import Flask
from Stochastic import *
import random
app = Flask(__name__)

@app.route('/')
def index():
    tempStringArr = stripFile()
    tupleValues = tuplegram(tempStringArr)
    values = createSentence(tupleValues, random.randint(10,31))
    return values
