#! /usr/bin/python
# -*- coding: utf-8 -*-

# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

str = raw_input("Input a sample string: ")

length = len(str)

l_str = str[:length/2]
r_str = str[length/2+1:]

if l_str == r_str[::-1]:
    print str, " is palindrom"
else:
    print str, " is no not palindrom"
