#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct  2 10:59:49 2019

@author: kofi meighan/km3547 and isabelle arevalo/ia2422
"""
vowels = 'aeiou'
user_input = input("Please input a word you'd like to translate to pig latin:")
def piggify(user_input):
    if user_input[0] in vowels :
        user_input += ("yay")
        return user_input
    else:
        for i,letter in enumerate(user_input): #instead of creating a count variable. i, (letter), incriments the counter for the index you're looking at
            if letter in vowels:
                letters_before_vowel = user_input[0:i]
                letters_after_vowel = user_input[i:]
                final_word = letters_after_vowel + letters_before_vowel + "ay"
                return final_word
        words_wo_vowels = user_input + "ay"
        return words_wo_vowels     
       


while user_input != ".": #terminating line
    print(piggify(user_input)) #if just (piggify(user_input)) it won't print anything and the world  would just sit in the program
    user_input = (input("Please enter another word to translate:"))
    

    