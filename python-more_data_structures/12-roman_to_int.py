#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    list_ = list(roman_string)
    sum_roman = 0
    i = 0
    while i < len(list_):
        if list_[i] != "I" and list_[i - 1] == "I" and i - 1 >= 0:
            sum_roman -= 2
        if list_[i] == "X":
            sum_roman += 10
        if list_[i] == "V":
            sum_roman += 5
        if list_[i] == "L":
            sum_roman += 50
        if list_[i] == "C":
            sum_roman += 100
        if list_[i] == "M":
            sum_roman += 1000
        if list_[i] == "I":
            sum_roman += 1
        if list_[i] == "D":
            sum_roman += 500
        i += 1
    return sum_roman
