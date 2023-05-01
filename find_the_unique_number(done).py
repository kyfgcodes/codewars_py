'''There is an array with some numbers. All numbers are equal except for one. Try to find it!'''

def find_uniq(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
    



print(find_uniq([ 0, 0, 0, 0, 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0, 1]))

#Technically done
