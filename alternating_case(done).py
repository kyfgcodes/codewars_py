
'''Define String.prototype.toAlternatingCase (or a similar function/method such as to_alternating_case/toAlternatingCase/ToAlternatingCase in your selected language; see the initial solution for details) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

"hello world".toAlternatingCase() === "HELLO WORLD"
"HELLO WORLD".toAlternatingCase() === "hello world"'''

# def to_alternating_case(string):
#    return string.swapcase()
def to_alternating_case(string):
    strn = ""
    for i in string:
        if i.isupper():
            strn += i.lower()
        else:
            strn += i.upper()
    return strn
        
           

print(to_alternating_case("hEllO i Am Telt"))

#Done!!!!

