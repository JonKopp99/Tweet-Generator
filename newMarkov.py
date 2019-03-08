from dictogram import Dictogram
import random
from Stochastic import *
from Modules import *
import re

def dicto(words):
    theDict = {}
    for word in words:
        if word not in theDict.keys():
            theDict[word] = {}
    index = 0
    for word in words:
        if len(words) > index + 1:
            next = words[index + 1]
            if next in theDict[word].keys():
                theDict[word][next] += 1
            else:
                theDict[word][next] = 1
            index += 1
    return theDict

def randWalk(amount, dict):
    sentence = random.choice(list(dict)).capitalize()
    ctr = 0
    while(ctr < amount):
        dictogram = random.choice(list(dict))
        sentence += (" " + dictogram.lower())
        ctr += 1
    sentence += random.choice([".","!"])
    return sentence

if __name__ == "__main__":
    words = stripFile()
    dictograms = dicto(words)
    test = randWalk(10, dictograms)
    print(test)
    #print(dictograms)
    #print(dictograms)
    #sentence = randWalk(random.randint(4,30),dictograms)
    #print(sentence)
