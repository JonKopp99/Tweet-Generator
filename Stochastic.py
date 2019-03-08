from Modules import *
import random

def sample(histogram):

    itemsInArray = 0.0
    for tple in histogram:
        itemsInArray += tple[1]
    ran_target = random.uniform(0, 1)
    #print(ran_target)

    total_prob = float(0.0)
    for tple in histogram:
        total_prob += float(tple[1])  / itemsInArray
        #print(total_prob)
        if(total_prob >= ran_target):
            return tple[0]

def sampleDict(dict):
    sum = 0
    #print(dict.values())
    for d in dict.items():
        for i in d:
            print(i.value)
    print(sum)


def testRuns(histogram):
    cumulative_dict = {}

    for tple in histogram:
        cumulative_dict[tple[0]] = 0


    ctr = 0
    while(ctr<=10000):
        cumulative_dict[sample(histogram)] += 1
        ctr+=1

    return cumulative_dict

def createSentence(histogram, amount):
    theSentence = ""
    ctr = 0
    while(ctr <= amount):
        word = sample(histogram)
        #theSentence  = theSentence + " ", word
        theSentence += " "
        theSentence += word
        ctr += 1

    theSentence += "."
    return theSentence
if __name__ == '__main__':
    tempStringArr = stripFile()#["one", "fish", "two", "fish","red", "fish","blue","fish"]


    tupleValues = tuplegram(tempStringArr)
    #print(tupleValues)

    #print(sample(tupleValues))

    #value = testRuns(tupleValues)
    print(createSentence(tupleValues, 20))
