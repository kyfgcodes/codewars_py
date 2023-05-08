'''I have a cat and a dog.

I got them at the same time as kitten/puppy. That was humanYears years ago.

Return their respective ages now as [humanYears,catYears,dogYears]'''


def human_years_cat_years_dog_years(human_years):
    animal_years = 0
    cat_age  = 0
    dog_age = 0
    if human_years == 1:
        cat_age = 15
        dog_age = 15
        return f'[{human_years},{cat_age},{dog_age}]'
    elif human_years == 2:
        cat_age = 24
        dog_age = 24
        return f'[{human_years},{cat_age},{dog_age}]'
    else:
        for i in range(human_years +1):

        #return f'[{human_years},{cat_age},{dog_age}]'
    
#Struggling


#print(human_years_cat_years_dog_years(10))


