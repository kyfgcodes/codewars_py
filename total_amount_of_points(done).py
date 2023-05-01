'''Our football team has finished the championship.

Our team's match results are recorded in a collection of strings. Each match is represented by a string in the format "x:y", where x is our team's score and y is our opponents score.

For example: ["3:1", "2:2", "0:1", ...]

scores are awarded for each match as follows:

if x > y: 3 scores (win)
if x < y: 0 scores (loss)
if x = y: 1 score (tie)
We need to write a function that takes this collection and returns the number of scores our team (x) got in the championship by the rules given above.'''


def scores(games):

    x_points = 0

    for score in games:
        if score[0] > score[-1]:
            x_points += 3
        elif score[0] < score[-1:]:
            continue
        else:
            x_points += 1
    return x_points


print(scores(['1:1', '2:2', '3:3', '4:4', '2:2',
      '3:3', '4:4', '3:3', '4:4', '4:4']))

#Done!!!