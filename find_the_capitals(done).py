'''Write a function that takes a single string (word) as argument. The function must return an ordered list containing the indexes of all capital letters in the string.'''

def capitals(word):
    uppers = []
    for i in range(len(word)):
        if word[i].isupper():
            [i] #convert to index of capital
            uppers.append(i) #append index
    return uppers


print(capitals('CodEWaRs'))

#Done!!!