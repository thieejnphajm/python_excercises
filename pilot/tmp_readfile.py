#! /usr/local/bin/python
# -*- coding: utf-8 -*-

file_path = 'numbers.txt'

with open(file_path, 'r') as open_file:
    numbers = []

    line = open_file.readline()

    while line:
        numbers.append(int(line))
        line = open_file.readline()

    print numbers;

