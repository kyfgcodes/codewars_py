'''Given two integers a and b, which can be positive or negative, find the sum of all the integers between and including them and return it. If the two numbers are equal return a or b.'''

def get_sum(a, b):
    neg_range = []
    pos_range = []
    if a == b:
        return a
    if b < 0:
        for i in range(a, b -1, -1):
            neg_range.append(i)
    if a < 0 and b < 0:
        for i in range(a, b -1, + 1 ):
            neg_range.append(i)


    else :
        for i in range(a, b + 1):
            pos_range.append(i)
    
    
print(get_sum(-3350,-750))    

  

