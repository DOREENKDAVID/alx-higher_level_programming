#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    score_weight = sum([num[0] * num[1] for num in my_list])
    weighted_mean = score_weight / sum([num[1] for num in my_list])
    return result
