#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    else:
        a_dictionary['key_max'] = max(a_dictionary)
        return a_dictionary['key_max']
