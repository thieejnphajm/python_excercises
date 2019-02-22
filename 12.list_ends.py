#! /usr/bin/python
# -*- coding: utf-8 -*-

# Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25])
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

import random

number = int(raw_input("Length of the list: "))

my_list = random.sample(range(100), number)

def first_last(your_list):
    return [your_list[0], your_list[-1]];

result = first_last(my_list)

print "The generated list is: ", my_list

print "The result is: ", result
