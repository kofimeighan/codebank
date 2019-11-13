 #!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:07:04 2019

@KOFIMEIGHAN
"""
user_input = str(input("Please type a word:"))

def print_box(s):
    x = s.split("\n")
    length_of_x = len(x[0]) #y
    
    for element in x:
        if len(element) > length_of_x:
            length_of_x = (len(element))
    longest_string = length_of_x+4 #z
    
    if "\n" in s :
        print('*' *longest_string)
        for element in x:
            if length_of_x != len(element):
                j = int((length_of_x-len(element))/2)
                space_left = (' '*j)
                if(length_of_x-len(element))%2 != 0:
                    j += 1
                space_right = (' '*j)
                print('* ' + space_left + element + space_right + ' *')
            else:
                print('* '+ element+' *')
        print('*'*longest_string)
    else:
        print('*'*longest_string)
        for element in x:
            print('* ' + element +' *')
        print('*'*longest_string)
   
    #for element in z:
       # print('*' + element + '*')
   # print('*'*y)
        

print_box(user_input)
  
