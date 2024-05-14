#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum_ = 0
    unique_list = list(set(my_list))
    for i in range(len(unique_list)):
        sum_ += unique_list[i]
    return sum_
