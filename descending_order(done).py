'''Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.'''

def descending_order(num):
    num_to_string = str(num)
    num_to_list = list(num_to_string)
    num_to_list.sort(reverse = True)
    list_to_str = ''.join(num_to_list)
    str_to_int = int(list_to_str)

    
    return str_to_int
   

  
print(descending_order(123456789))

#Done!!!