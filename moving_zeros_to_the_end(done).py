'''Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.'''

def move_zeros(lst):
    no_zeros = []
    zeros = []
    for i in lst:
        if i != 0:
            no_zeros.append(i)
        elif i == 0:
            zeros.append(i)

    no_zeros.extend(zeros)
    return no_zeros

print(move_zeros([0, 8, 5 ]))

#Done!!!