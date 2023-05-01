'''Write a function which calculates the average of the numbers in a given list.'''

def find_average(numbers):
    if []:
        return 0
    return sum(numbers) / len(numbers)


print(find_average([1, 2, 3]))

#Done!!!!