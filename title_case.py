'''Write a function that will convert a string into title case, given an optional list of exceptions (minor words). The list of minor words will be given as a string with each word separated by a space. Your function should ignore the case of the minor words string -- it should behave in the same way even if the case of the minor word string is changed.'''


def title_case(title, minor_words=''):
    title = title.split()
    first_word = title[0].upper()
    words = []
    for i in title:
       for i in range(1, len(title)):
          
            words.append(i)

    words.append(i)
    return f'{words}, {first_word}'
        
    


  


print(title_case('a clash of KINGS', 'a an the of'))