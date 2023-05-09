#1'''Implement a pseudo-encryption algorithm which given a string S and an integer N concatenates all the odd-indexed characters of S with all the even-indexed characters of S, this process should be repeated N times.'''

'''Together with the encryption function, you should also implement a decryption function which reverses the process.

If the string S is an empty value or the integer N is not positive, return the first argument without changes.

'''


def decrypt(encrypted_text, n):
    pass


def encrypt(text, n):
    for x in range(n + 1):
        odd = [x for x in text if text.index(x) % 2 == 1]
        even = [x for x in text if text.index(x) % 2 == 0]
        e_list = odd + even
    

            
        return e_list


    pass


print(encrypt("012345", 2))

#Struggling