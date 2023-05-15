'''As a part of this Kata, you need to create a function that when provided with a triplet, returns the index of the numerical element that lies between the other two elements.

The input to the function will be an array of three distinct numbers (Haskell: a tuple).

For example:

gimme([2, 3, 1]) => 0
2 is the number that fits between 1 and 3 and the index of 2 in the input array is 0.'''

def gimme(input_array):
    middle_el = ''
    if input_array[-2] > input_array[-1]:
        middle_el += input_array(0)
        return input_array.index(middle_el)
    else:
        return 1


   


print(gimme([2, 3, 1]))

#Struggling