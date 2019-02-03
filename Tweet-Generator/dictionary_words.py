import random, sys

def rearrange(amount):
    tempStringArr = [line.strip() for line in open('/usr/share/dict/words')]
    randomArr = []
    #loop through array and append to new in random order.
    for k in range(amount):
        rand_string = random.choice(tempStringArr)
        randomArr.append(rand_string)

    return randomArr

if __name__ == '__main__':
    params = sys.argv
    amount = int(params[1])
    newString = ' '.join(rearrange(amount))
    print(newString)
