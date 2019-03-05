#! /usr/local/bin/python
# -*- coding: utf-8 -*-

# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series.
# The other exercises are: Part 1, Part 3, and Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe board.
# However, this is significantly more than half an hour of coding, so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game of Tic Tac Toe,
# not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = [[1, 2, 0],
# 	[2, 1, 0],
# 	[2, 1, 1]]
# where a 0 means an empty square, a 1 means that player 1 put their token in that space,
# and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe game board,
# tell me whether anyone has won, and tell me which player won, if any. A Tic Tac Toe win is 3 in a row - either in a
# row, a column, or a diagonal. Don’t worry about the case where TWO people have won - assume that in every board there
# will only be one winner.

game = [[2, 2, 2],
	[2, 1, 0],
	[2, 1, 1]]

def check_row(row):
    return len(set(row)) <= 1

def check_colums(game, cols):
    columns = []
    for i in range(len(game)):
        columns.append(game[i][cols])
    return len(set(columns)) <= 1

def check_mate(game):
    length = len(game)
    cross_1 = []
    cross_2 = []
    for i in range(length):
        if check_row(game[i]):
            return game[i][0]
        elif check_colums(game, i):
            return game[0][i]
        else:
            cross_1.append(game[i][i])
            cross_2.append(game[-(i+1)][i])

    if len(set(cross_1)) <= 1:
        return cross_1[0]

    if len(set(cross_2)) <= 1:
        return cross_2[0]

    return 0

print check_mate(game)
