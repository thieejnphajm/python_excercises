#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# In a previous exercise, we’ve written a program that “knows” a number and asks a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100.
# The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it took to get your number.

# As the writer of this program, you will have to choose how your program will strategically guess.
# A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
# But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the
# range), and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal
# strategy! (We’ll talk about what is the optimal one next week with the solution.)

import random

MINIMUM = 0
MAXIMUM = 101

TRY = 1

GUESS = 50

while True:
    answer = raw_input("Is this your number %s? " %GUESS).lower()
    if 'no' in answer  and 'higher' in answer:
        MINIMUM = GUESS + 1
        GUESS = (GUESS + MAXIMUM + 1) / 2
    elif 'no' in answer and 'lower' in answer:
        MAXIMUM = GUESS - 1
        GUESS = (GUESS + MINIMUM) / 2
    elif 'no' == answer:
        more_answer = raw_input("higher or lower? ").lower()
        if 'higher' == more_answer:
            MINIMUM = GUESS + 1
            GUESS = (GUESS + MAXIMUM + 1) / 2
        elif 'lower' == more_answer:
            MAXIMUM = GUESS - 1
            GUESS = (GUESS + MINIMUM) / 2

    elif 'yes' == answer:
        print 'Bravo, Just try %d times to guess number %s' %(TRY, GUESS)
        break

    TRY += 1
