#! /usr/bin/python

number = int(raw_input("Put a number:"))

if number % 2 == 0:
    print 'This number is even'
else:
    print 'This number is odd'

num = int(raw_input("Put another number"))
check = int(raw_input("Put check value"))

if num % check == 0 and (num / check) % 2 == 0:
    print 'This is special number'

