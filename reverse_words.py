'''Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.'''


def reverse_words(text):
   text = text[::-1]
   r_index = 0
   r_words = ''

   for i in text:
      r_words += i + r_words(r_index)
      r_index + 1

   
   
   return r_words

print(reverse_words('double  spaces'))
#Struggling