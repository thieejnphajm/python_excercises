#! /usr/bin/python
# -*- coding: utf-8 -*-

# Write a program (function!) that takes a list and returns a new list that contains all the elements of the first
# list minus all the duplicates.

# Extras:

#     Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#     Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import random

num = int(raw_input("Input the length of randoms: "))

randoms = [random.randrange(10) for i in range(num)];

print "Randoms list: ", randoms

# By set
randoms_set = list(set(randoms))
print "Randoms set: ", randoms_set

# By loop
nodup_randoms = []

for i in randoms:
    if i not in nodup_randoms:
        nodup_randoms.append(i);

print "No dup randoms: ", nodup_randoms
