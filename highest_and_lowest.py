'''In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.'''


def high_and_low(numbers):
   number_list = []

   if not '':
      for i in numbers:
         number_list.append(int(i))
   return number_list 

      


print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))
#Struggling with this one
    