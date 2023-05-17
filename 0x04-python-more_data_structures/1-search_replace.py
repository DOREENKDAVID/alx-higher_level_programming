#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = []
    for elem in my list:
        if elem is search:
            new_list.append(replace)
        else:
            new_list.append(elem)
    return new_list
