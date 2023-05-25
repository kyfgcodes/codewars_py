import re
'''Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.'''


def increment_string(strng):
    zeros = ''.join([x for x in strng if x == '0'])
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
    num = int(str_num) + 1
    new_strng = ''
    for i in reversed(strng):
       if i.isalpha():
           break
       new_strng += i
   
    if num >= 10:
        zeros = zeros.replace('0', '', 1)
       
        return f"{new_strng}{zeros}{num}"
    #elif:
    else:
        return f"{new_strng}{zeros}{num}"
    
    
   
    #return zero_fill,num  



print(increment_string('fo99obar99'))

#Struggling