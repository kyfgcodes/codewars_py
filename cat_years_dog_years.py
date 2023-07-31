'''I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]'''


def human_years_cat_years_dog_years(human_years):
    
    if human_years == 1:
        return [1, 15, 15]
    
    elif human_years == 2:
        return [2, 24, 24]
    
    else:
        older_cat_age =  24 
        older_dog_age = 24
        for _ in range(human_years - 2):
           
            older_cat_age += 4
            older_dog_age += 5

    return [human_years,older_cat_age,older_dog_age]

print(human_years_cat_years_dog_years(4))




