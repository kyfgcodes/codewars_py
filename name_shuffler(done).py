'''Write a function that returns a string in which firstname is swapped with last name.'''

def name_shuffler(str_):
    names = str_.split()
    return ' '.join(names[::-1])


print(name_shuffler("john McClane"))

#Done!!!