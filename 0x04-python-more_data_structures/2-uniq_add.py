#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique = []
    add = 0
    for elem in my_list:
        if elem not in unique:
            unique.append(elem)
            add += elem
    return add
