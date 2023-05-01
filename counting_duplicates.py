'''Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.'''

def duplicate_count(text):
    dupe_count = 0
    occurence_count = 0 
    for letter in text:
        if text.count(letter) > 1:
            occurence_count += 1
            if occurence_count >= 2:
                dupe_count += 1
                occurence_count = 0


    return dupe_count 


print(duplicate_count("abcdeaB"))

#Struggling with this one
