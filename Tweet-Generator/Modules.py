
#A histogram() function which takes a source_text argument (can be either a filename or the contents
#of the file as a string, your choice) and return a histogram data structure that stores each unique
#word along with the number of times the word appears in the source text.
def dict_togram(theWords):
    histoDict = {}
    currentIndex = 0 #Keeps track of location in array
    for word in theWords:
        wordIndex = currentIndex + 1 #tracks location of what word we are comparing
        ctr = 1
        while(wordIndex < len(theWords)): #Loop through to compare
            if(theWords[wordIndex] == word):
                theWords.pop(wordIndex) #Remove duplicates from arr (no need to keep)
                ctr += 1
            wordIndex += 1

        currentIndex += 1
        histoDict.update( {word : ctr} )
    return histoDict

def listtogram(theWords):
    completeWordList = list()
    currentIndex = 0 #Keeps track of location in array
    for word in theWords:
        wordIndex = currentIndex + 1 #tracks location of what word we are comparing
        ctr = 1
        wordArrElement = [word]
        while(wordIndex < len(theWords)): #Loop through to compare
            if(theWords[wordIndex] == word):
                theWords.pop(wordIndex) #Remove duplicates from arr (no need to keep)
                ctr += 1
            wordIndex += 1

        currentIndex += 1
        wordArrElement.append(ctr)
        completeWordList.append(wordArrElement)
    return completeWordList

def tuplegram(theWords):
    completeWordList = list()
    currentIndex = 0 #Keeps track of location in array
    for word in theWords:
        wordIndex = currentIndex + 1 #tracks location of what word we are comparing
        ctr = 1
        while(wordIndex < len(theWords)): #Loop through to compare
            if(theWords[wordIndex] == word):
                theWords.pop(wordIndex) #Remove duplicates from arr (no need to keep)
                ctr += 1
            wordIndex += 1

        currentIndex += 1
        wordTuple = (word,ctr)
        completeWordList.append(wordTuple)
    return completeWordList

#A unique_words() function that takes a histogram argument and returns the total count of unique words
#in the histogram. For example, when given the histogram for The Adventures of Sherlock Holmes, it returns the integer 8475.
def unique_words(theWords):
    ctr = 0
    currentIndex = 0 #Keeps track of location in array
    for word in theWords:
        wordIndex = currentIndex + 1 #tracks location of what word we are comparing
        ctr += 1
        while(wordIndex < len(theWords)): #Loop through to compare
            if(theWords[wordIndex] == word):
                theWords.pop(wordIndex) #Remove duplicates from arr (no need to keep)
            wordIndex += 1
        currentIndex += 1
    return ctr

#A frequency() function that takes a word and histogram argument and returns the number of times that word appears in a text.
#For example, when given the word "mystery" and the Holmes histogram, it will return the integer 20.
def frequency(word, theWords):
    ctr = 0
    for i in theWords:
        if(i == word):
            ctr += 1

    return ctr


if __name__ == '__main__':
    tempStringArr = ["one", "fish", "two", "fish","red", "fish","blue","fish"]

    #dictionary test
    #dictionaryValue = dict_togram(tempStringArr)
    #print(dictionaryValue)

    #unique words test
    #countOfUniqueWords = unique_words(tempStringArr)
    #print(countOfUniqueWords)

    #frequency test
    freq = frequency("fish", tempStringArr)
    print(freq)

    #matrix list test
    #listValues = listtogram(tempStringArr)
    #print(listValues)

    #tuple tetst
    #tupleValues = tuplegram(tempStringArr)
    #print(tupleValues)
