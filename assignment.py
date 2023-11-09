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
        instructions = input("\033[1;35;40m Do you want the instructions? yes or no: ").lower().replace(" ", "")
        if instructions == "no":
           print ("Alright, lets go!")
           break 
        elif instructions== "yes":
           print ("These are the instructions! The program will ask you what you want to calculate\nThen, it will ask you the inputs needed.\nLet's Go! ")
           break 
        else: 
           print ("Invalid input. Please enter yes or no")
    return None
<<<<<<< HEAD

def start(): #Player chooses which function to execute
    while True:
        Ins='Type a number to commence the specific function.\n:'
        VC='\n  Volume Calculations:\n           Sphere==>1\n             Cube==>2\nRectangular Prism==>3\n             Cone==>4'
        SAC='\n\nSurface Area Calculations:\n               Sphere==>5\n                 Cube==>6\n    Rectangular Prism==>7\n                 Cone==>8'
        PT='\n\nPythagorean Theorem==>9\n'
        TotalInstructions=VC+SAC+PT+Ins
        choice=input(TotalInstructions)
        try:
            choice=int(choice)
            if 0<choice<=9:
                return choice
            else:
                print('Invalid input\nYou must input an integer between 1 and 9.\n')
        except:
            print('Invalid input\nYou must input an integer between 1 and 9.\n')
choice=start()
=======
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
>>>>>>> 32a25bfc6558d869fa304f82875c302364c90434


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

