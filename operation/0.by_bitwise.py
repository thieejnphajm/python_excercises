#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import random

def add(number1, number2):
    remain = number1 & number2
    result = number1 ^ number2
    while remain != 0:
        return add(remain << 1, result)
    return result

def sub(number1, number2):
    if number1 < number2:
        return -sub(number2, number1)

    borrow = ~number1 & number2
    result = number1 ^ number2
    while borrow != 0:
        return sub(result, borrow << 1)
    return result

def multiply(number1, number2):
    result = 0
    for i in range(0, number2):
        result += number1
    return result

def devide(number1, number2):
    result = 0
    while number1 >= number2:
        result += 1
        number1 = sub(number1, number2)
    return result

def modulo(number1, number2):
    while number1 >= number2:
        number1 = sub(number1, number2)
    return number1

number1 = random.choice(range(100))
number2 = random.choice(range(100))

print 'Add:      {} + {} = {}'.format(number1, number2, add(number1, number2))
print 'Sub:      {} - {} = {}'.format(number1, number2, sub(number1, number2))
print 'Multiply: {} x {} = {}'.format(number1, number2, multiply(number1, number2))
print 'Devide:   {} / {} = {}'.format(number1, number2, devide(number1, number2))
print 'Modulo:   {} % {} = {}'.format(number1, number2, modulo(number1, number2))

