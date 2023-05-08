'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.'''

def find_short(s):
    short = s.split()
    for i in short:
        if len(i) == min(short):
            return i
            




print(find_short('i am short'))

#Still struggling