''' When writing on Twitter, he is known for almost always capitalizing every word. For simplicity, you'll have to capitalize each word.'''

def to_jaden_case(string):
    str_list = list(string.split(' '))
    jaden_list = []
    for i in str_list:
        jaden_list.append(i.capitalize())
    
    final_str = ' '.join(map(str, jaden_list)) #So useful for turning lists into strings!!


    return final_str



print(to_jaden_case('hi i am bob'))

#Done!!!
