#! /usr/bin/python
# -*- coding: utf-8 -*-

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only
# the elements that are common between the lists (without duplicates).
# Make sure your program works on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if
# you can’t figure this out at this point - we’ll get to it soon)
# number  = int(raw_input("Input a number: "))

from random import randint

length_a = randint(1, 20)

length_b = randint(1, 20)

a = list(randint(1, 100) for i in range(0, length_a))
b = list(randint(1, 100) for i in range(0, length_b))

print("a: ", a)
print("b: ", b)

commons = set()

for i in a:
    if i in b:
        commons.add(i)

print("Commons: ", list(commons))
