'''Given a random non-negative number, you have to return the digits of this number within an array in reverse order.'''
def digitize(n):
   n_to_str = str(n)
   num_list = list(n_to_str)
   
   return num_list[::-1]




print(digitize(12345))
#Done!!!!
