'''There was a test in your class and you passed it. Congratulations!
But you're an ambitious person. You want to know if you're better than the average student in your class.

You receive an array with your peers' test scores. Now calculate the average and compare your score!

Return True if you're better, else False!'''


def better_than_average(class_points, your_points):
    if sum(class_points) / len(class_points) < your_points:
        return True
    return False


print(better_than_average([100, 40, 34, 57, 29, 72, 57, 88], 75))


#Done!!!!!