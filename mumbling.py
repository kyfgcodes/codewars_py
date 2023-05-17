'''accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"'''


def accum(s):
    s = s.split()
    index_count = 1
    ls = ''
    for i in range( index_count + 1):
        for i in s:
            ls += i
    return ls

#Struggling

print(accum('abcd'))