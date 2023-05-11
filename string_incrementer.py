import re
'''Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.'''

def increment_string(strng):
    # strng = [x for x in strng]
    # test = []
    # for i in reversed(strng):
    #     if i.isalpha():
    #         break

    #     test.append(i)

    if not strng:
        return '1'
    if not strng[-1].isdigit():
        return f'{strng}1'
    
    strng = ''
    num = ''

    for i in reversed(strng):
        if i.isalpha():
            break
        num += i
    

    return  num



print(increment_string('foo99obar99'))

#Struggling