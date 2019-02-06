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
            print("Target")
            return tple[0]
def testRuns(histogram):
    cumulative_dict = {}

    for tple in histogram:
        cumulative_dict[tple[0]] = 0


    ctr = 0
    while(ctr<=10000):
        cumulative_dict[sample(histogram)] += 1
        ctr+=1

    print(cumulative_dict)


if __name__ == '__main__':
    tempStringArr = ["one", "fish", "two", "fish","red", "fish","blue","fish"]


    tupleValues = tuplegram(tempStringArr)
    print(tupleValues)

    #print(sample(tupleValues))

    testRuns(tupleValues)
