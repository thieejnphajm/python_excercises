#! /usr/bin/python
from datetime import datetime

name = raw_input("What is your name?:")
age = int(raw_input("How old are you?:"))

year = int(100 - age + datetime.now().year)

# print(name + " will be 100 years old in year " + year)
message = ("%s will be 100 years old in year %d" %(name, year))
print message

count = int(raw_input('Many message?:'))

print((message + '\n')*count)
