'''Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours! Otherwise, you can be sure he's not...'''



def friend(x):
    friends = []
    for name in x:
        friends.append(name)
        if len(name) != 4:
            friends.remove(name)
    return friends

print(friend(["Ryan", "Jimmy", "123", "4", "Cool Man"]))

#Done!!!

