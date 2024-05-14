#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            new_list += True,
        else:
            new_list += False,
    print(new_list)
    return new_list
