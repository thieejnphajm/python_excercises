#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Selection sort
# Select min value and increase swap

# numbers = [1,5,2,4,3,6]
# numbers = [6,5,4,3,2,1]

import random

MAX_NUMBER = 10

numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]
# numbers = random.sample(range(100), 10)

# numbers = [99, 80, 27, 73, 78]
# numbers = [1,2,3,4,5,6,7]

print "Before: ", numbers

def selection_sort(numbers):
    length = len(numbers)

    unsorted = True
    for i in range(1, length):
        if numbers[i] < numbers[i-1]:
            unsorted = False
            break

    if unsorted:
        return numbers

    for i in range(length - 1):
        min_index = i
        for j in range(i+1, length):
            if numbers[j] < numbers[min_index]:
                min_index = j
        print 'Min index: ', min_index
        if min_index != i:
            numbers[i], numbers[min_index] = numbers[min_index], numbers[i]

    return numbers

selection_sort(numbers)

print "After: ", numbers
