#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Insertion sort

# From 2nd shift if not that big

# numbers = [1,5,2,4,3,6]
# numbers = [6,5,4,3,2,1]

import random

MAX_NUMBER = 10

numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]
# numbers = random.sample(range(100), 10)

# numbers = [99, 80, 27, 73, 78]

print "Before: ", numbers

length = len(numbers)

for i in range(1, length):
    tmp = numbers[i]

    for j in range(0, i)[::-1]:
        if tmp < numbers[j]:
            numbers[j+1] = numbers[j]
            if j == 0:
                numbers[j] = tmp
        else:
            numbers[j+1] = tmp
            break

print "After: ", numbers
