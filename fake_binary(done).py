'''Given a string of digits, you should replace any digit below 5 with '0' and any digit 5 and above with '1'. Return the resulting string.'''

def fake_bin(x):
   num_list = []
   for i in x:
      if i >= '5':
         num_list.append('1')
      elif i < '5':
         num_list.append('0')

   return ''.join(num_list)
    
    
   
        
    
print(fake_bin("800857237867"))

#Done!!!!
 