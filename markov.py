from dictogram import Dictogram
import random
import Stochastic
from Modules import *
import re
def dicto(words):
    dict = {}
    for index in range(len(words) -1):
        if words[index] not in dict:
            dict[words[index]] = Dictogram()
        else:
            dict[words[index]].add_count(words[index+1])
    return dict

def randWalk(amount, dict):
    sentence = ""
    ctr = 0
    while(ctr < amount):
        dictogram = random.choice(list(dict))
        sentence += (" " + dictogram)
        ctr += 1
    return sentence
if __name__ == "__main__":
    words = stripFile()
    dictograms = dicto(words)
    #print(dictograms)
    sentence = randWalk(15,dictograms)
    print(sentence)
