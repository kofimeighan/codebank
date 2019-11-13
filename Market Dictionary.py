 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 3 15:07:04 2019

@author: kofi meighan/km3547 
"""
def read_markets(FILENAME):
    zip_to_market = {}
    town_to_zips = {}
    f = open('/Users/kofimeighan/Documents/E1006/markets.txt','r')#FILENAME, 'r')
    for line in f:
        market_details = line.strip().split('#')
        zip_code = market_details[4]
        market_name = market_details[0],market_details[1], market_details[2], market_details[3], zip_code
        zip_to_market[zip_code] = [market_name] 
        town = market_details[3]
        town_to_zips[town] = zip_code  
    return zip_to_market , town_to_zips

def print_market(market):
    market_list = []
    for i in market[0]:
        market_list.append(i)
    market_string = ("{}\n{}\n{}, {} {}").format(market_list[1],market_list[2],market_list[3],market_list[0],market_list[4])
    return print(market_string)

if __name__ == "__main__":
    FILENAME = "markets.txt"
    try: 
        zip_to_market, town_to_zips = read_markets(FILENAME)
        x = 0
        read_markets(FILENAME)
        while x == 0:
            user_input = input("Please enter a zip code or a town name, or type quit to exit the program:")
            
            if user_input == "quit":
                break
            elif user_input.isdigit():
                if user_input in zip_to_market:
                    zip_to_market_input = (zip_to_market[user_input])
                    for i in zip_to_market_input:
                        print_market(zip_to_market_input)
                else:
                    print('Zip code not found.')
            elif user_input in town_to_zips:
                user_input_town = town_to_zips[user_input]
                returned_market_name = (zip_to_market[user_input_town]) 
                print_market(returned_market_name)
            elif user_input not in town_to_zips:
                print('Town not found.')
            elif user_input.isdigit() == False:
                 print('Zip code not found.')

    except (FileNotFoundError, IOError):
        print("Error reading {}".format(FILENAME))