#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to
# largest) and another number. The function decides whether or not the given number is inside the list and returns
# (then prints) an appropriate boolean.

# Extras:
#     Use binary search.


def binary_search(x, numbers, left, right):
    mid = (left + right) / 2
    if x == numbers[mid]:
        return mid;
    elif left > right or x < numbers[left] or x > numbers[right]:
        return -1;
    elif x > numbers[mid]:
        return binary_search(x, numbers, mid+1, right)
    else:
        return binary_search(x, numbers, left, mid-1)

numbers = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7,  9, 10]

x = int(raw_input("Input a number to search: "))

def second_at(x, numbers):
    found_at = binary_search(x, numbers, 0, len(numbers)-1)
    if found_at == -1:
        return -1;
    first_at = found_at

    while first_at > 0 and numbers[first_at - 1] == x:
        first_at -= 1;

    if found_at - first_at >= 1:
        return first_at + 1;

    if found_at + 1 < len(numbers) and numbers[found_at + 1] == x:
        return found_at + 1;

    return -1;

print second_at(x, numbers)
