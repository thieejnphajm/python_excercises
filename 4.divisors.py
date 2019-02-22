#! /usr/bin/python
# -*- coding: utf-8 -*-

# Create a program that asks the user for a number and then prints out a list of
# all the divisors of that number. (If you don't know what a divisor is, it is a
# number that divides evenly into another number. For example, 13 is a divisor of
# 26 because 26 / 13 has no remainder.)

number  = int(raw_input("Input a number: "))

divisors = []

divisors.append(1)

for candidate in range(2, (number/2+1)):
    if number % candidate == 0:
        divisors.append(candidate)

divisors.append(number)

print("Divisors: %s" % divisors)
