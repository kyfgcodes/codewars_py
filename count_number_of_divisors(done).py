'''Count the number of divisors of a positive integer n.
4 --> 3 (1, 2, 4)'''

def divisors(n):
    divisor_count = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisor_count += 1
    return divisor_count

#Done!!!



print(divisors(5))

#Struggling with this one