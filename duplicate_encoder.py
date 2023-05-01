'''The goal of this exercise is to convert a string to a new string where each character in the new string is "(" if that character appears only once in the original string, or ")" if that character appears more than once in the original string. Ignore capitalization when determining if a character is a duplicate.'''


def duplicate_encode(word):
    new_word = []

    for i in word:
        if word.count(i) >= 2:
            new_word.append(')')
        elif word.count(i) == 1:
            new_word.append('(')
    return ''.join(new_word)


print(duplicate_encode('success'))

#Struggling with this one