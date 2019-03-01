#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Merge sort
# Break into 2 smaller, sort then merge

# numbers = [1,5,2,4,3,6]
# numbers = [6,5,4,3,2,1]

import random

MAX_NUMBER = 10

# numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]
# numbers = random.sample(range(100), 10)

# numbers = [99, 80, 27, 73, 78]
# numbers = [1,2,3,4,5,6,7]

def check_sorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False
    return True

def merge(numbers_1, numbers_2):
    numbers = []
    index_1 = index_2 = 0
    length_1 = len(numbers_1)
    length_2 = len(numbers_2)
    longer = length_1 if length_1 > length_2 else length_2

    while index_1 < length_1 or index_2 < length_2:
        if index_1 >= length_1:
            numbers.append(numbers_2[index_2])
            index_2 += 1
        elif index_2 >= length_2:
            numbers.append(numbers_1[index_1])
            index_1 += 1
        elif numbers_1[index_1] <= numbers_2[index_2]:
            numbers.append(numbers_1[index_1])
            index_1 += 1
        else:
            numbers.append(numbers_2[index_2])
            index_2 += 1
    return numbers

def merge_sort(numbers):
    length = len(numbers)
    if length <= 1:
        return numbers
    return merge(merge_sort(numbers[:length/2]), merge_sort(numbers[length/2:]))

again = 0

while again < 10:
    # numbers = random.sample(range(100), 10)
    numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]
    print "Before: ", numbers
    numbers = merge_sort(numbers)
    print "After: ", numbers

    print "In sorted? ", 'Yes' if check_sorted(numbers) else 'No'

    again += 1

