'''Write a function that takes an array of strings as an argument and returns a sorted array containing the same strings, ordered from shortest to longest.'''



def sort_by_length(arr):
    shortest_first = []

    min_len = 30
    for ele in arr:
        if len(ele) < min_len:
            min_len = len(ele)
            shortest_first.append(ele)
    
    return shortest_first







print(sort_by_length(["Telescopes", "Glasses", "Eyes", "Monocles"]))