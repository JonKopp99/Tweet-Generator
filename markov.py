from dictogram import Dictogram
import random
import Stochastic
from Modules import *

def dicto(words):
    dict = {}
    for index in range(len(words) -1):
        if words[index] not in dict:
            dict[words[index]] = Dictogram()
        else:
            dict[words[index]].add_count(words[index+1])
    return dict

if __name__ == "__main__":
    words = stripFile()
    dictograms = dicto(words)
    print(dictograms)
