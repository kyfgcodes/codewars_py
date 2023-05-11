'''In this little assignment you are given a string of space separated numbers, and have to return the highest and lowest number.'''


def high_and_low(numbers):
  numbrs = []
  for i in numbers:
    if i != '':
      i = int(i)
      numbrs.append(i)
  neg = []
  pos = []
  for i in numbers:
    if i != '' and i > '0':
      pos.append(i)
    elif i == '-':
      continue
    neg.append(i)


  return numbrs
    
    
      


print(high_and_low("6 7"))
#Struggling with this one
    