'''A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.'''

def is_pangram(s):
    s = s.lower()
    alpha = set(['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
    alpha_list = []
    set_alpha_list = set(alpha_list)

    for i in s:
        if i in alpha:
            alpha_list.append(i)
    set_alpha_list = set(alpha_list)

    if alpha.difference(set_alpha_list):
        return False
    return True

#Done!!!
    


    
        
#Struggling with this one
             

    # if alpha_count >= 26:
    #     return True
    # elif alpha_count < 26:
    #     return False




print(is_pangram('Cwm fjord bank glyphs vext quiz'))