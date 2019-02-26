#! /usr/local/bin/python
# -*- coding: utf-8 -*-

import random

def fill_letter(guess, word, letter):
    for i in range(len(word)):
        if letter == word[i]:
            guess[i] = letter.upper()
    return guess

with open('./sowpods.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words).strip()

guess = ['_']*len(word)

print ''.join(guess)

while '_' in guess:
    letter = raw_input('Gess your letter: ').upper()
    if letter in guess:
        print 'Another letter please!'
    elif letter not in word:
        print 'Incorrect!'
    else:
        guess = fill_letter(guess, word, letter)
        print ''.join(guess)

