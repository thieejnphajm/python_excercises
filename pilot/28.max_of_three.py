#! /usr/local/bin/python
# -*- coding: utf-8 -*-

def find_max(a,b,c):
    tmp = a
    if tmp < b:
        tmp = b
    if tmp < c:
        tmp = c
    return tmp

x = raw_input("Input 3 numbers: ")

xs = x.strip().split(' ')

print 'Max is {}'.format(find_max(xs[0], xs[1], xs[2]))
