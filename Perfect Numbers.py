#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 25 12:03:03 2019

@author: kofimeighan/3547
"""

number = int(input("Please type a number to test if it is a perfect number:"))
x = 1
i=2
while i < number:
    if (number%i) == 0:
        x = x+i
    i=i+1
    
if x == number:
    print("Your number is a perfect numebr!")
else:
    print("Your number is not a perfect number :(")

