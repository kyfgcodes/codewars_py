'''Given a string, you have to return a string in which each character (case-sensitive) is repeated once.'''
# word = input("type a word:" )

# for i in word:
#     print(i + i, end= '')


def double_char(s):
     return ''.join(letter * 2 for letter in s)

        
    
print(double_char("1234!_ "))

#Done!!!




