'''In this kata you will create a function that takes a list of non-negative integers and strings and returns a new list with the strings filtered out.'''

def filter_list(l):
    filtered_list = []
    for char in l:
        if type(char) == float or type(char) == int:
            filtered_list.append(char)
    return filtered_list #Note that the return function belongs to the loop
   
    
print(filter_list([1,2,3, "ahgfj", True,False]))

#Done!!!!

