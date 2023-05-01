'''Given an array of integers.

Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers. 0 is neither positive nor negative.

If the input is an empty array or is null, return an empty array.'''


def count_positives_sum_negatives(arr):
    positive_count = 0
    negatives = []
    for num in arr:
        if num > 0:
            positive_count += 1
    for num in arr:
        if num < 0:
            negatives.append(num)
    sum_of_negatives = sum(negatives)
    total = positive_count,sum_of_negatives
    return list(total)

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -1, -1, -1, -1]))
#Done!!!!