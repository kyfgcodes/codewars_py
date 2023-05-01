'''Create a function called shortcut to remove the lowercase vowels (a, e, i, o, u ) in a given string.'''


def shortcut(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    str_without_vowel = []
    for i in s:
        if i.lower() and i in vowels:
            pass
        if i not in vowels:
            str_without_vowel.append(i)
    return ''.join(str_without_vowel)


print(shortcut("hello"))

#Done!!!!