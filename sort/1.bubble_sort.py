#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Bubble sort

# numbers = [1,5,2,4,3,6]
# try to bubble bigger number by always swap adjacent element

import random
def bubble_sort(numbers):
    length = len(numbers)
    for i in range(length):
        for j in range(1, length - i):
            if numbers[j] < numbers[j-1]:
                numbers[j], numbers[j-1] = numbers[j-1], numbers[j]
    return numbers

# list of non duplicated numbers
# numbers = random.sample(range(100), 10)


# list of duplicated numbers
MAX_NUMBER = 20
numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]

print "Before: ", numbers
print "After:  ", bubble_sort(numbers)
