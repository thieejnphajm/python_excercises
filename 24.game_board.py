#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other exercises are: Part 2, Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that look like this:

#     --- --- ---
#    |   |   |   |
#     --- --- ---
#    |   |   |   |
#     --- --- ---
#    |   |   |   |
#     --- --- ---

# This one is 3x3 (like in tic tac toe). Obviously, they come in many other sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them to the screen using Python’s print statement.

def print_horizon(size):
    horizon = ' '
    for _ in range(0, size):
        horizon += '--- '

    print horizon

def print_vertical(size):
    vertical = '|'
    for _ in range(size):
        vertical += '   |'
    print vertical


def print_go(size):
    print_horizon(size)

    for _ in range(size):
        print_vertical(size)
        print_horizon(size)

size = int(raw_input("Size of the GO: "))
print_go(size)
