'''Write a function that removes the spaces from the string, then return the resultant string.'''


def no_space(x):
    x_no_space = ''
    for i in x:
        x_no_space += i.replace(' ', '')
    return x_no_space


print(no_space('hi iiim k'))

#Done!!!

#Alt solution:

#return x.replace(' ', '')