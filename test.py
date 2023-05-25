def increment_string(strng):
    arrnum = []

    strng = strng[::-1]

    for i in strng:
        if i.isdigit():
            arrnum.append(i)
        break

    if len(arrnum) == 0:
        return strng[::-1] + '1'
    
    else:
        arrnum = arrnum[::-1]
        strng = strng[len(arrnum):]

        arrnum = str(int(''.join(arrnum))+ 1).zfill(len(arrnum))
        return strng[::-1] + arrnum