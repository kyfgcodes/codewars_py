import re
"""Complete the solution so that the function will break up camel casing, using a space between words."""

# While loop breaks program !!!!

#nested for loop
def solution(s):
    first_word = ''
    capital_words = ''
    for i in s:
        if i.isupper():
            s = s.split(first_word)
            s =''.join([str(item) for item in s])
            break
        first_word += i
    #return s
    for i in s:
        capital_words += i
    capital_words = ' '.join([item for item in re.split("([A-Z][^A-Z]*)", capital_words) if item])
    
    return f'{first_word} {capital_words}'


print(solution("helloWorldNot"))


#Done!!!
