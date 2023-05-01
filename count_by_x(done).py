'''Create a function with two arguments that will return an array of the first n multiples of x.

Assume both the given number and the number of times to count will be positive numbers greater than 0.'''

def count_by(x, n):
    multiples = []
    for i in range(1, n + 1):
        multiple = i * x
        multiples.append(multiple)
        i += 1
    return multiples


print(count_by(2, 5))

#Done!!!