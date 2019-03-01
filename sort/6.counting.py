#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Merge sort
# Break into 2 smaller, sort then merge

# numbers = [1,5,2,4,3,6]
# numbers = [6,5,4,3,2,1]

import random

MAX_NUMBER = 10000

# numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]
# numbers = random.sample(range(100), 10)

# numbers = [99, 80, 27, 73, 78]
# numbers = [1,2,3,4,5,6,7]

def check_sorted(numbers):
    for i in range(1, len(numbers)):
        if numbers[i] < numbers[i-1]:
            return False
    return True

def counting_sort(numbers):
    minimum = min(numbers)
    maximum = max(numbers)

    length = maximum - minimum + 1

    counts = [0]*length

    for number in numbers:
        counts[number - minimum] += 1


    sum_counts = sum(counts)

    tmp = counts[-1]
    for i in range(1, length)[::-1]:
        tmp = counts[i]
        counts[i] = sum_counts
        sum_counts -= tmp

    results = [0]*len(numbers)
    for number in numbers:
        index = counts[number - minimum] - 1
        results[index] = number
        counts[number - minimum] -= 1

    return results

again = 0

while again < 10:
    # numbers = random.sample(range(100), 10)
    numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]
    # numbers = [8, 5, 0, 9, 5, 8, 6, 9, 5, 3]
    # print "Before: ", numbers
    numbers = counting_sort(numbers)
    # print "After: ", numbers

    # print "In sorted? ", 'Yes' if check_sorted(numbers) else 'No'
    if not check_sorted(numbers):
        print 'No'
        print numbers
        break
    else:
        print again

    again += 1

