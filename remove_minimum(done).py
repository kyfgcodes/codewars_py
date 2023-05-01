'''Task
Given an array of integers, remove the smallest value. Do not mutate the original array/list. If there are multiple elements with the same value, remove the one with a lower index. If you get an empty array/list, return an empty array/list.

Don't change the order of the elements that are left.'''

#First attempt
# def remove_smallest(numbers):
#     if []:
#         return []
#     numbers_without_min = []
    
#     for i in numbers:
#        numbers_without_min.append(i)
#     numbers_without_min.remove(min(numbers_without_min))
    
#     return numbers_without_min

# print(remove_smallest([1, 2, 3, 1, 1]))
#Done!!!!


#Refactor (doesn't count because we mutate original list)
def remove_smallest(numbers):
    if not numbers:
        return []
    numbers.remove(min(numbers))
    return numbers

print(remove_smallest([1, 2, 3, 1, 1]))