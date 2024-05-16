#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    i = 0
    c = 0
    while i < list_length:
        try:
            c = my_list_1[i] / my_list_2[i]
        except IndexError:
            print("out of range")
            c = 0
        except ZeroDivisionError:
            print("division by 0")
            c = 0
        except TypeError:
            print("wrong type")
            c = 0
        finally:
            i += 1
            new_list.append(c)
    return new_list
