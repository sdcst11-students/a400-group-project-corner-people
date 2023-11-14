#!python3
# Volume Calculator
# Feel free to rename your variables

import math 

def title():
    titlePage='\033[1;32m\n\n   Kimby\'s Python Calculator\n      By: Ruby and Kimmie\n          Calculates:'
    calculators='\033[1;34m\n            Volume,\n         Surface Area,\n           And More!\n'
    print(titlePage,calculators)
    return None

def instructions():
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


#these are all the specific calculation functions 
def Vsphere():
        while True: 
            rad= input(" \033[0;33;47m \nWe will calculate the volume of your sphere! \nPlease input your radius, it must be a positive number: ")
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
        side= input("\nWe will calculate the volume of your cube! \nPlease input your side, it must be a positive number: ")
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

def VrecPri():
    print("We will calculate the volume of your rectangular prism!")
    while True: 
        l=input('What is the length of your prism?\n')
        w=input('What is the width of your prism?\n')
        h=input('What is the height of your prism?\n')
        try:
            l=float(l)
            w=float(w)
            h=float(h)
            if l<=0 or w<=0 or h<=0:
                print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.')
                break
            answerVRP= l*h*w
            print(f'The surface area of a rectangular prism with side lengths {l}, {w}, and {h} is {answerVRP}')
            break 
        except:
            print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.')

def Vcone():
    print ("We will calculate the volume of your cone!")
    while True: 
        rad= input('What is the radius of your cone?\n')
        height= input('What is the height of your cone?\n')
        try:
            rad=float(rad)
            height=float(height)
            if rad <= 0 or height <= 0:
                print ("Invalid Input(s). Please enter correct input(s): ")
            else:
                answerVCone= round(math.pi * (rad **2)* (height/3),2)
                print (f'The volume of a cone with a radius of {rad} and a height of {height} is {answerVCone}. ')
                break
        except:
                print ("Invalid Input(s). Please enter correct input(s): ")

def SA_Cone():
    print('\nWe will calculate the surface area of your cone!\nYou will need to input 2 positive values\nfor the radius of the base, and height.')
    while True: 
        rad= input("Please input the radius of the base, it must be a positive number: ")
        height=input("Please input the height of the cone: ")
        try:
            rad=float(rad)
            height=float(height)
            if rad <= 0 or height <= 0: 
                print ("Invalid Input(s). Please enter valid value(s). ")
            else:
                answerSACone= (math.pi*rad**2)+math.sqrt(rad**2 + height **2)*rad*math.pi
                answerSACone=round(answerSACone,2)
                print (f'The surface area of a cone with a radius of {rad} and a height of {height} is {answerSACone}.')
                
                break
        except:
                print ("Invalid Input(s). Please enter valid number(s). ")

def SA_cube():
    print('\nWe will calculate the surface area of your cube! \nPlease input your side, it must be a positive number: .')
    while True: 
        side= input("Please input your side, it must be a positive number: ")
        try:
            side=float(side)
            if side <= 0: 
                print ("Invalid Input. Please enter valid value: ")
            else:
                answerSAC= 6 * side **2
                print (f'The surface area of a cube with a side length of {side} is {answerSAC}.')
                break
        except:
                print ("Invalid Input. Please enter valid number: ")

def SA_RecPrism():
    print('\nWe will calculate the surface area of a rectangular prism.\nYou will need to input 3 positive values for the length,\nwidth, and height:')
    while True:
        l=input('What is the length of your prism?\n')
        w=input('What is the width of your prism?\n')
        h=input('What is the height of your prism?\n')
        try:
            l=float(l)
            w=float(w)
            h=float(h)
            if l<=0 or w<=0 or h<=0:
                print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.')
                break
            answerSAP=2 * (l*w+l*h+w*h)
            print(f'The surface area of a rectangular prism with side lengths {l}, {w}, and {h} is {answerSAP}')
            break
        except:
            print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.')

def SA_Sphere():
    print('\nWe will calculate the surface area of a sphere.\nYou will need to input 1 positive value for the radius.')
    while True: 
        rad= input("Please input your radius, it must be a positive value: ")
        try:
            rad=float(rad)
            if rad <= 0: 
                print ("Invalid Input. Please enter valid input: ")
            else:
                answerSAS= 4 * math.pi* (rad ** 2)
                answerSAS=round(answerSAS,2)
                print (f'The surface area of a sphere with radius {rad} is {answerSAS}')
                break
        except:
            print ("Invalid Input. Please enter valid input: ")

def PyTheorem():
    print('We will find the missing side length of a right\ntriangle using the pythagorean theorem. You\nmust input 2 positive values.')
    while True:
        length=input('Are you looking for the hypotenuse, which is\nthe side opposite to the right angle? Yes/No: ')
        length=length.lower()
        length=length.replace(' ','')
        if length=='yes':
            side1=input('What is the first side length: ')
            side2=input('What is the second side length: ')
            try:
                side1=float(side1)
                side2=float(side2)
                if side1 <= 0 or side2<= 0: 
                    print ("Invalid Input(s). Please enter valid input: ")
                else:
                    hyp= round(math.sqrt(side1**2+side2**2,2))
                    print(f'The hypotenuse of a triangle with known side lengths of {side1} and {side2} is {hyp}.')
                    break
            except:
                print('Invalid inputs')
        elif length=='no':
            hyp=input('What is the hypotenuse length: ')
            side1=input('What is the known side length: ')
            try:
                hyp=float(hyp)
                side1=float(side1)
                if side1 <= 0 or hyp<= 0: 
                    print ("Invalid Input(s). Please enter valid input: ")
                else:
                    side2=round(math.sqrt(hyp**2-side1**2),2)
                    print(f'The missing side length of a triangle with known side of {side1} and hypotenuse of {hyp} is {side2}.')
                    break
            except:
                print('Invalid input(s).')
        else:
            print('Invalid answer, you must input either yes or no.')

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    title()
    instructions()
    while True:
        choice=start()
        functionList=('nil',Vsphere,Vcube,VrecPri,Vcone,SA_Cone,SA_cube,SA_RecPrism,SA_Sphere,PyTheorem)
        functionList[choice]()
        end=input('Do you wish to end your session? yes or no: ')
        end=end.lower()
        end=end.replace(' ','')
        if end=='yes':
            break


if __name__ == "__main__":
    main()

