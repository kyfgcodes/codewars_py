import re
'''Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.'''

def increment_string(strng):
    if not strng.isdigit():
        return f'{strng}1'
    
    if not any(char.isdigit() for char in strng):
        return f'{strng}1'
    
    else:
        num = [x for x in strng if x.isdigit()]
        add_num = int("".join(num))
        new_str = ''.join([x for x in strng if x.isalpha()])

        return f'{new_str}{add_num + 1}'

    
#Struggling


print(increment_string('foo001'))