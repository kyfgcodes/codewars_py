'''Create a function that accepts a string and a single character, and returns an integer of the count of occurrences the 2nd argument is found in the first one.

If no occurrences can be found, a count of 0 should be returned.'''

def str_count(strng, letter):
    l_count = strng.count(letter)
    return l_count


print(str_count('', '1'))

#Done!!!