#! /usr/bin/python
# -*- coding: utf-8 -*-

# Write a program (using functions!) that asks the user for a long string containing multiple words.
# Print back to the user the same string, except with the words in backwards order.
# For example, say I type the string:

#   My name is Michele
# Then I would see the string:

#   Michele is name My
# shown back to me.

sentence = raw_input("Type a sentence with spaces: ")

def reverse_sentence(sentence):
    return ' '.join(sentence.split(' ')[::-1])

print "Sentence: ", sentence
print "Reverse sentence: ", reverse_sentence(sentence)
