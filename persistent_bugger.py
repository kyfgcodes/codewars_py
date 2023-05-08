'''Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence, which is the number of times you must multiply the digits in num until you reach a single digit.'''

def persistence(n):
    n = [x for x in str(n)]
    pers = 0
    num = 0
    while num in range(0, 9):
       num +=  n[0] * n[-1]
       pers += 1
    return pers

print(persistence(39))

#Struggling