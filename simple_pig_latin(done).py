'''Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.'''

def pig_it(text):

    word_list = text.split()
    words = []

    for word in word_list:
        if word.isalpha(): 
            pig = word[1:]+word[0]+ "ay"
            words.append(pig)
        elif words:
            words.append(word)

    
    
    words_str = ' '.join(words)


    return words_str
        

print(pig_it('pig latin is cool !'))

#Done