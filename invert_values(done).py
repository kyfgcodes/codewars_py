'''Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.'''

def invert(lst):
    inverted_vals = []
    for i in lst:
        inverted_vals.append(i * -1)
    return inverted_vals

print(invert([1, -2]))

#Done!!!