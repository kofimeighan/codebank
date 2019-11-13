#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 15 18:19:05 2019

@KOFIMEIGHAN
"""
def select_meal():
    user_input = str(input("Hello! Would you like a pizza or a salad?"))
    meals = []
    while user_input != "done":
        if user_input == "pizza":
            meals.append(pizza())
        elif user_input == "salad":
            meals.append(salad())
        order = ("Your order is a {}" + " and a {}"*(len(meals)-1)).format(*meals) + "."
        user_input = input(order + "Place another order for pizza by saying 'pizza' or for salad by saying 'salad' or say done to complete your order.")
    return "Your order has been placed. Goodbye." 
            
def pizza():
    pizza_size = str( input("Small Medium or Large?"))
    toppings_result = pizza_size + toppings()
    return toppings_result 

def toppings():
    toppings = [str(input("Add a topping:pepperoni, mushrooms, spinach, or say done:"))]
    additional_toppings = 0
    while additional_toppings != "done":
            additional_toppings = str(input("Add another topping or say done:"))
            if additional_toppings != "done":
                toppings.append(additional_toppings)
    return (' pizza with {}' + ' and {}'*(len(toppings)-1)).format(*toppings)
        
def salad():
    type_of_salad = str(input("Would you like a garden salad or a greek salad?"))
    dressing_result = dressing()
    return type_of_salad + " salad with " + dressing_result #+ dressing_choice + " dressing"

def dressing():
    dressing_choice = str(input("Please choose a dressing: vinaigrette, ranch, blue cheese, lemon:")) + " dressing"
    return dressing_choice
        
    
    
    
