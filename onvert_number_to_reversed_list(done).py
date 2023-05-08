'''Given a random non-negative number, you have to return the digits of this number within an array in reverse order.'''


def digitize(n):
    n = str(n)
    n = [x for x in n]
    reversed_list = []
    for i in reversed(n):
        reversed_list.append(int(i))
    return reversed_list

#Done!!!

print(digitize(35231))