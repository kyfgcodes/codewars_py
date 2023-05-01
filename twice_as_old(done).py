'''Your function takes two arguments:

current father's age (years)
current age of his son (years)
calculate how many years ago the father was twice as old as his son (or in how many years he will be twice as old). The answer is always greater or equal to 0, no matter if it was in the past or it is in the future.'''

def twice_as_old(dad_years_old, son_years_old):
    son_doubled = son_years_old * 2
    how_old_dad = (dad_years_old - son_doubled)
    how_old_dad = int(str(how_old_dad).replace('-', '')) #Have to remove - for code wars 

    return how_old_dad


print(twice_as_old(55,30))


#Done!!!!