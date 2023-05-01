import math
'''The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.'''


def century(year):
   century = year / 100
   if century / 2 != 0:
     return int(math.ceil(century))
   

print(century(1901))


#Done!!!!