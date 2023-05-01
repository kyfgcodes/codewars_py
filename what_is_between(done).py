'''Complete the function that takes two integers (a, b, where a < b) and return an array of all integers between the input parameters, including them.'''


def between(a,b):

    all_in_between = []
    
    for i in range(a, b + 1):
        all_in_between.append(i)
    return all_in_between
        
    

print(between(1, 4))

#Done!!!!