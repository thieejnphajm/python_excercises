#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Selection sort
# Select min value and increase swap

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

def quick_sort(numbers):
    if len(numbers) <= 1:
        return numbers
    pivot = numbers[-1]
    left = 0
    right = len(numbers) - 2

    while left <= right:
        if numbers[left] <= pivot:
            left += 1
            continue

        if numbers[right] > pivot:
            right -= 1
            continue

        numbers[left], numbers[right] = numbers[right], numbers[left]

    numbers[left], numbers[-1] = numbers[-1], numbers[left]
    return quick_sort(numbers[0:left]) + quick_sort(numbers[left:])

again = 0

while again < 10:
    # numbers = random.sample(range(100), 10)
    numbers = [random.choice(range(MAX_NUMBER)) for _ in range(MAX_NUMBER)]
    print "Before: ", numbers
    numbers = quick_sort(numbers)
    print "After: ", numbers

    print "In sorted? ", 'Yes' if check_sorted(numbers) else 'No'

    again += 1

