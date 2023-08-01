'''Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.'''

def abbrev_name(name):
    name = name.upper().split()
    abr = ''
    for i in name:
        abr += i[0]
    return '.'.join(abr)




print(abbrev_name('Aj Galler'))

#Finished