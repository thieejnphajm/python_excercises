#! /usr/bin/python
# -*- coding: utf-8 -*-

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
# the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the
# sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

count = int(raw_input("Number of Fibonnaci that you want to generate: "))

fibos = []

for i in range(0, count):
    if i in [1,0]:
        fibos.append(1);
    else:
        fibos.append(fibos[i-1] + fibos[i-2]);

print fibos;
