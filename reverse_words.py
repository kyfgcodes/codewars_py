'''Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.'''


def reverse_words(text):
    r_words = ''
    for i in reversed(text):
        r_words += i
    #return r_words

    reversed_words = r_words[-1::] + r_words[0::]

    return reversed_words

print(reverse_words('double  spaces'))
#Struggling