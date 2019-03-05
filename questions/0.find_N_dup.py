#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import string
import random

def check_n_dup(str, n):
    tmp = {}

    for i in range(len(str)):
        if tmp.has_key(str[i]):
            tmp[str[i]] += 1
            if tmp[str[i]] == n:
                return i
        else:
            tmp[str[i]] = 1

    return None;

templates = string.letters

str = ''.join(random.choice(string.letters) for _ in range(random.choice(range(20))))
str = 'abcdabcabc'

print 'String: ', str

print "Check duplicate at: ", check_n_dup(str, 2)
