#!python3
# Volume Calculator
# Feel free to rename your variables

import math 

def title():
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title
    titlePage='\033[1;32m\n\n   Kimby\'s Python Calculator\n      By: Ruby and Kimmie\n          Calculates:'
    calculators='\033[1;34m\n            Volume,\n         Surface Area,\n           And More!\n'
    print(titlePage,calculators)
    return None

def instructions():
    # Will display instructions
    # input parameters: none needed
    # output parameters: None
    # Author:
    # Modified:
    while True:
        instructions = input("Do you want the instructions? yes or no: ").lower().replace(" ", "")
        if instructions == "no":
           print ("Alright, lets go!")
           break 
        elif instructions== "yes":
           print ("These are the instructions! The program will ask you what you want to calculate\nThen, it will ask you the inputs needed.\nLet's Go! ")
           break 
        else: 
           print ("Invalid input. Please enter yes or no")
    return None
def Vsphere():
    while True: 
        rad= input("We will calculate the volume of your sphere! \nPlease input your radius, it must be a positive number: ")
        try:
            rad=float(rad)
            if rad <= 0: 
                print ("Invalid Input. Please enter correct input: ")
            else:
                answerVS= round ((4/3)* math.pi* (rad ** 3), 2)
                print (f'The volume of a sphere with radius {rad} is {answerVS}')
                break 
        except:
                print ("Invalid Input. Please enter correct input: ")
    return None 
def Vcube():
    while True: 
        side= input("We will calculate the volume of your cube! \nPlease input your side, it must be a positive number: ")
        try:
            side=float(side)
            if side <= 0: 
                print ("Invalid Input. Please enter correct input: ")
            else:
                answerVC= side**3
                print (f'The volume of a cube with a side of {side} is {answerVC}')
                break
        except:
                print ("Invalid Input. Please enter correct input: ")
    return None 


def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    instructions()
    Vsphere()
    Vcube()

if __name__ == "__main__":
    main()

