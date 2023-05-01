'''The main idea is to count all the occurring characters in a string. If you have a string like aba, then the result should be {'a': 2, 'b': 1}.

What if the string is empty? Then the result should be empty object literal, {}.'''


def count(s):
    final_count ={}
    if not s:
        return {}
    
    if s:
        for i in s:
            final_count.update({i:s.count(i)})
        
        
    return final_count
        
print(count('aabb'))

#Done!!!
