"""Complete the solution so that the function will break up camel casing, using a space between words."""

# While loop breaks program !!!!


def solution(s):

    first_word = ''
    

    for i in s:
        if not i.isupper():
            first_word += i
        else:
            break
    second_word  = s.replace(first_word, '')

    return second_word
        


        
   
    
        

   


print(solution("iamNot"))


# Try using yield
