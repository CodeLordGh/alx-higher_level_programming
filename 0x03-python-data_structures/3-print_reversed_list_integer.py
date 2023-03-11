#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    number_of_elements = len(my_list)
    for i in range(number_of_elements-1, -1, -1):
        print("{:d}".format(my_list[i]))
