import re
'''Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.'''


def increment_string(strng):
    zero_counter = str(strng.count('0'))
    if not strng:
        return '1'
    if not strng[-1].isdigit():
        return f'{strng}1'
    
    num = []
    
    for i in reversed(strng):
       if i.isalpha():
           break
       num.append(i)
    
    str_num = (''.join([x for x in reversed(num)]))
    new_strng = strng.replace(str_num, '')
    num = int(str_num) + 1
    if num >= 10:
        less_zero_counter = str(strng.count('0')- 1)
        zero_fill = new_strng.zfill(len(less_zero_counter))
    else:
        zero_fill = new_strng.zfill(len(zero_counter))
    
    
   
    return f'{zero_fill}{num}',  num, zero_counter



print(increment_string('foo008'))

#Struggling