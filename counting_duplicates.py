"""Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits."""


def duplicate_count(text):
    new_text = [x for x in text]  # list comprehension
    dupe_count = 0
    dupe_list = []
    occurence_count = 0

    for i in new_text:
        if new_text.count(i) >= 2:
            dupe_count += 1
            dupe_list.append(i)
            occurence_count += 1
        if occurence_count == 1:
            dupe_count -= 1
            occurence_count = 0

    return dupe_count


print(duplicate_count("iiss"))

# Struggling with this one
