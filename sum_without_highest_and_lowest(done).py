'''Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.'''

def sum_array(arr):
    if not arr:
        return 0
    if len(arr) == 1:
        return 0
    arr.sort()
    arr.pop(0)
    arr.pop()

    return sum(arr)
print(sum_array([1]))


#Done!!!!