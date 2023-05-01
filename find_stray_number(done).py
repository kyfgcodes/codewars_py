'''You are given an odd-length array of integers, in which all of them are the same, except for one single number.

Complete the method which accepts such an array, and returns that single different number.'''

def stray(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
  



print(stray([2, 3, 2, 2, 2]))

#Done!!!
