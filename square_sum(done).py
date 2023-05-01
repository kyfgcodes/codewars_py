'''Complete the square sum function so that it squares each number passed into it and then sums the results together.
'''

def square_and_sum(numbers):
    squared_nums = []
    for i in numbers:
        squared_nums.append(i ** 2)
    return sum(squared_nums)

print(square_and_sum(([0, 3, 4, 5])))

#Done!!!