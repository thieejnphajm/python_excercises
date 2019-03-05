#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import random
with open('./sowpods.txt', 'r') as f:
    words = f.readlines()

print random.choice(words).strip()

