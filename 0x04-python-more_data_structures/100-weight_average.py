#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    n = 0
    for i, v in enumerate(my_list):
        sum += v[0] * v[1]
        n += v[1]
    return sum / n
