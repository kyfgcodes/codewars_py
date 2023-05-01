'''Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.'''

def spin_words(sentence):
    sen_to_list = sentence.split()
    reverse_words = []
    for i in sen_to_list:
        if len(i) < 5:
            reverse_words.append(i)
        elif len(i) >= 5:
            reverse_words.append(i[::-1])

    final_string = ' '.join(reverse_words)

    return final_string



print(spin_words("This sentence is a sentence"))

#Done!!!


   






#  return ' '.join(list) 