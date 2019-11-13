# -*- coding: utf-8 -*-
"""
Spyder Editor

@KOFIMEIGHAN.
"""

import random

player_move = input("Please type (r)ock, (p)aper, or (s)cissors: ")

computer_move = random.choice(['r','p','s'])

print("Computer chose "+computer_move)

if (player_move == computer_move):
    print("Draw.")
if (player_move == "r" and computer_move == "p"):
    print("Computer wins.")
if (player_move == "p" and computer_move == "s"):
    print("Computer wins.")
if (player_move == "s" and computer_move == "r"):
    print("Computer wins.")
if (player_move == "r" and computer_move == "s"):
    print("Player wins.")
if (player_move == "p" and computer_move == "r"):
    print("Player wins.")
if (player_move == "s" and computer_move == "p"):
    print("Player wins.")