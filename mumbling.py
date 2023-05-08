'''accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"'''


def accum(s):
    index_count = 0
    ls = ''
    for i in s:
        ls =+ i * index_count
    return ls

#Struggling

print(accum('abcd'))