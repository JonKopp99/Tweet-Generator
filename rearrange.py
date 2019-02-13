import random, sys

def rearrange(theString):
    tempStringArr = theString.split(' ')
    randomArr = []
    #loop through array and append to new in random order.
    for k in range(len(tempStringArr)):
        rand_string = random.choice(tempStringArr)
        tempStringArr.pop(tempStringArr.index(rand_string))
        randomArr.append(rand_string)

    return randomArr

if __name__ == '__main__':
    newStirng = ' '.join(rearrange("how now brown cow"))
    print(newStirng)
