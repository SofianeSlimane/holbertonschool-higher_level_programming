#!/usr/bin/python3
def multiple_returns(sentence):
    my_tuple = len(sentence),
    if len(sentence) == 0:
        my_tuple += None,
    else:
        my_tuple += sentence[0],
    return my_tuple
