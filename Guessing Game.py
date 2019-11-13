#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 21 14:17:56 2019

@author: kofimeighan
"""

import random
computer_move = int(random.randint(1,10)) #random module
#9print(computer_move) #delete later, for console notes






player_move = int(input("Type a number bertween 1 and 10:")) #making player input number, turning it to an integer
difference = abs(player_move - computer_move) #setting variable for the difference between input and random guess

#if player_move < 1 or player_move > 10 : #making sure the user puts in correct input
   # print("Invalid input!")      
    #^^^not needed because it checks invalid input within the loop
    
iteration_counter = 1
while difference > 0 and iteration_counter <= 5: #START OF LOOP

    if player_move < 1 or player_move > 10 : #second invalid input within the loop
        print("Invalid input!") #needed because the first invalid input is not within the loop 
    else:
        if difference < 3:
                print("Almost there!")
        elif difference <= 5:
                print("Close.")
        elif difference > 5:
                print("Not even close.")
        
    player_move = int(input("Try another number:"))
    difference = abs(player_move - computer_move)
    iteration_counter = iteration_counter + 1
    #print(iteration_counter)
    
if iteration_counter == 6 :
    print("You ran out of guesses!")
    
else:
    print("You win!")  
        
     
     
        
    
        
    
