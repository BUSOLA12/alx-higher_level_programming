#!/usr/bin/python3

def search_replace(my_list, search, replace):

    result = [my_list.replace(x, replace) for x in my_list if x == search]
    return result
