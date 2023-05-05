"""Given a non-negative integer, 3 for example, return a string with a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers."""


def count_sheep(n):
    sheep = ""

    for i in n:
        sheep += f"{i}...sheep"
    return sheep


print(count_sheep(2))
