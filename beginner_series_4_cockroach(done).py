
'''The cockroach is one of the fastest insects. Write a function which takes its speed in km per hour and returns it in cm per second, rounded down to the integer (= floored).'''

def cockroach_speed(s):
    cm_per_second = s * (27.7778)
    return int(cm_per_second)
  

print(cockroach_speed(1.08))

#Done!!!!