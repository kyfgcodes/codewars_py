'''Take an array and remove every second element from the array. Always keep the first element and start removing with the next element.'''

def remove_every_other(my_list):
    return my_list[0::2] #start at first item, no stop, skip each 2nd item

print(remove_every_other([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))

#Done!!!