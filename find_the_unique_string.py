'''There is an array of strings. All strings contains similar letters except one. Try to find it!'''

def find_uniq(arr):
    for i in arr:
        if arr.count(i) == 1:
            return i
        

print(find_uniq([ 'Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a' ]))