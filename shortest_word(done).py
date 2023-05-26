'''Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.'''

def find_short(s):
    s = s.split() #turn string into list in order to be able to use min function
    s = ''.join((min(s, key = len))) #grab shortest word and turn back into string
    return len(s) #return length of shortest word - 3
    
   
    
     
            




print(find_short('bitcoin take over the world maybe who knows perhaps'))

#Done!!!