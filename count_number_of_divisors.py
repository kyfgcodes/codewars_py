'''Count the number of divisors of a positive integer n.
4 --> 3 (1, 2, 4)'''

def divisors(n):
    divisor_count = 0
    new_n = 0
    while new_n != n:
        for i in range(1, n + 1):
            if i % n == 0:
                divisor_count += 1
            new_n += 1
    return divisor_count




print(divisors(4))

#Struggling with this one