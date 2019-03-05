#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import string
import random

def check_first_dup(str):
    tmp = {}

    for i in range(len(str)):
        if tmp.has_key(str[i]):
            return i
        else:
            tmp[str[i]] = 1

    return None;

templates = string.letters

str = ''.join(random.choice(string.letters) for _ in range(random.choice(range(20))))

print 'String: ', str

print "First duplicate at: ", check_first_dup(str)
