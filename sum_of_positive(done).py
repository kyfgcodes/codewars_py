'''You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.'''

def positive_sum(arr):
    positive_nums = []
    for i in arr:
        if i > 0:
            positive_nums.append(i)
    if not positive_nums:
        return 0 
    return sum(positive_nums)

print(positive_sum([-1,-2,-3,-4,-5]))

#Done!!!