#! /usr/bin/python
# -*- coding: utf-8 -*-

# Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
# Take this opportunity to think about how you can use functions. Make sure to ask the user to enter
# the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the sequence is the
# sum of the previous two numbers in the sequence. The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

count = int(raw_input("Number of Fibonnaci that you want to generate: "))

fibos = []

def recur_fibo(num):
    if num <= 2:
        return 1;
    else:
        return recur_fibo(num-1) + recur_fibo(num-2);

for i in range(1, count+1):
    fibos.append(recur_fibo(i));

print fibos;
