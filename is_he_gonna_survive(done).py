'''A hero is on his way to the castle to complete his mission. However, he's been told that the castle is surrounded with a couple of powerful dragons! each dragon takes 2 bullets to be defeated, our hero has no idea how many bullets he should carry.. Assuming he's gonna grab a specific given number of bullets and move forward to fight another specific given number of dragons, will he survive?

Return True if yes, False otherwise :)'''

def hero(bullets, dragons):
    can_be_defeated = dragons * 2
    if can_be_defeated <= bullets:
        return True
    return False


print(hero(10, 5))

#Done!!!!