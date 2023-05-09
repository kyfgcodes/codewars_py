'''Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive integers. No floats or non-positive integers will be passed.'''


def sum_two_smallest_numbers(numbers):
    lowest = []
    for i in numbers:
        if i == min(numbers):
            lowest.append(i)
            numbers = numbers.remove(i)
    return lowest
        


print(sum_two_smallest_numbers([5, 8, 12, 18, 22]))

#Struggling