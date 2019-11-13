#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 19:03:07 2019

@author: kofimeighan
"""

print("Pick a number in your head. Now say whether the computer's guess is too large, too small or correct")
numbers = [1,2,3,4,5,6,7,8,9,10]
left = 0 #left bound
right = 9 #right bound
user_input = ("") #initialize the variable
guess_number = 1
while user_input != "correct" and guess_number < 4:
        print(numbers[int((right+left)/2)])
        user_input = input("Say whether the guess was 1)too big, 2)too small, 3)correct:")
    
        if user_input != "too big" and user_input != "too small" and user_input != "correct":
            print("Invalid input")
        elif user_input == ("too big"):
            right = ((right+left)/2)
            guess_number = (guess_number+1)
            
        elif user_input == ("too small"):
            left = ((right+left)/2)
            guess_number = (guess_number+1)
                
        elif (user_input == ("correct")):
            print("The computer won!")
            
if guess_number == 4 :
    print("The computer ran out of guesses :(")
    
        

