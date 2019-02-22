#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# Create a program that will play the “cows and bulls” game with the user.
# The game works like this:

# Randomly generate a 4-digit number.
# Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they have a “cow”.
# For every digit the user guessed correctly in the wrong place is a “bull.”
# Every time the user makes a guess, tell them how many “cows” and “bulls” they have.
# Once the user guesses the correct number, the game is over.
# Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

def cowbulls(number, guess):
    length = len(number)
    cow = []
    count_bull = 0

    number_a = list(number)
    guess_a = list(guess)

    for i in range(len(number)):
        if guess[i] == number[i]:
            cow.append(i)

    count_cow = len(cow);

    cow.reverse()
    for i in cow:
        del number_a[i]
        del guess_a[i]

    for i in number_a:
        if i in guess_a:
            count_bull = count_bull + 1
            guess_a.remove(i)

    print("Cow: %d, Bull: %d" % (count_cow, count_bull))

number = raw_input("Input number with 4 digit: ")
guess = raw_input("Input check with 4 digit: ")

cowbulls(number, guess)
