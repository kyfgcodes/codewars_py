'''It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string. You don't have to worry with strings with less than two characters.'''

def remove_char(s):
    remove_first_and_last = s[1:-1]  #The slicing starts at the  first letter and ends on the last letter, taking the first and last letter.
    
    return remove_first_and_last 


print(remove_char('eloquent'))

#Done!!!!