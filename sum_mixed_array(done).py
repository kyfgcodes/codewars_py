'''Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.

Return your answer as a number.
'''

def sum_mix(arr):
    all_num_list = []
    for i in arr:
        if i != type(int):
            all_num_list.append(int(i))
        else:
            all_num_list.append(i)
    return sum(all_num_list)

print(sum_mix([9, 3, '7', '3']))

#Done!!!