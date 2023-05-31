"""Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds."""


def clock(h, m, s):
    midnight =  (h * 36000000) + (m * 60000) + s
    return midnight




print(clock(0,1,1))
