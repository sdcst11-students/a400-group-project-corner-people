#!python3
# Volume Calculator
# Feel free to rename your variables

import math 

def title():
    titlePage='\033[1;32m\n\n   Kimby\'s Python Calculator\n      By: Ruby and Kimmie\n          Calculates:'
    calculators='\033[1;34m\n            Volume,\n         Surface Area,\n           And More!\n'
    quit ="\033[1;31;40mIf you would like to quit at any time, type \"quit\"\n Let's Go!"
    print(titlePage,calculators,quit)
    return None

def instructions():
    while True:
        instructions = input("\033[1;35;40mDo you want the instructions? yes or no: ").lower().replace(" ", "")

        if instructions == "no":
           print ("Alright, lets go!")
           return True 
        elif instructions== "yes":
           print ("These are the instructions! The program will ask you what you want to calculate\nThen, it will ask you the inputs needed.\n")
           return True 
        elif instructions=='quit': 
            return False
        else:
           print ("Invalid input. Please enter yes or no")

def start(): #Player chooses which function to execute
    while True:
        Ins='\033[1;31;40m Type a number to commence the specific function.\n:'
        VC='\033[1;32;40m Volume Calculations: ' 
        Vcho = '\033[1;30;40m \n           Sphere==>1\n             Cube==>2\nRectangular Prism==>3\n             Cone==>4'
        SAC='\033[1;32;40m \n\nSurface Area Calculations: '
        SAcho= '\033[1;30;40m\n               Sphere==>5\n                 Cube==>6\n    Rectangular Prism==>7\n                 Cone==>8'
        PT='\033[1;31;40m  \n\nPythagorean Theorem==>9\n'
        TotalInstructions=VC+Vcho+SAC+SAcho+PT+Ins
        choice=input(TotalInstructions).lower().replace(' ','')
        if choice=='quit':
            return 'quit'
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
            rad=input("\033[1;37;44m \nWe will calculate the volume of your sphere! \nPlease input your radius, it must be a positive number: ")
            rad=rad.lower().replace(' ','')
            if rad=='quit':
                return False
            try:
                rad=float(rad) 
                if rad <= 0: 
                    print ("\nInvalid Input. Please enter correct input. \n")
                else:
                    answerVS= round ((4/3)* math.pi* (rad ** 3), 2)
                    answerVS=round(answerVS,2)
                    print (f'The volume of a sphere with radius {rad} is {answerVS}')
                    break 
            except:
                print ("Invalid Input. Please enter correct input.\n ")
        return True 

def Vcube():
    while True: 
        side= input("\033[1;33;40m\nWe will calculate the volume of your cube! \nPlease input your side, it must be a positive number: ")
        side=side.lower().replace(' ','')
        if side=='quit':
            return False
        try:
            side=float(side)
            if side <= 0: 
                print ("Invalid Input. Please enter correct input.\n ")
            else:
                answerVC= side**3
                answerVC=round(answerVC,2)
                print (f'The volume of a cube with a side of {side} is {answerVC}')
                break
        except:
                print ("Invalid Input. Please enter correct input.\n ")
    return True

def VrecPri():
    print("\033[1;32;40mWe will calculate the volume of your rectangular prism!")
    while True: 
        l=input('What is the length of your prism?\n').lower().replace(' ','')
        if l=='quit':
            return False
        w=input('What is the width of your prism?\n').lower().replace(' ','')
        if w=='quit':
            return False
        h=input('What is the height of your prism?\n').lower().replace(' ','')
        if h=='quit':
            return False
        try:
            l=float(l)
            w=float(w)
            h=float(h)
            if l<=0 or w<=0 or h<=0:
                print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.\n')
            else:
                answerVRP= round(l*h*w,2)
                print(f'\nThe volume of a rectangular prism with side lengths {l}, {w}, and {h} is {answerVRP}')
                break 
        except:
            print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers\n')
    return True 

def Vcone():
    print ("\033[1;30;40m We will calculate the volume of your cone!")

    while True: 
        rad= input("Please input the radius of the base, it must be a positive number: ").lower().replace(' ','')
        if rad=='quit':
                    return False
        height=input("Please input the height of the cone: ").lower().replace(' ','')
        if height=='quit':
                return False
        try:
            rad=float(rad)
            height=float(height)
            if rad <= 0 or height <= 0:
                print ("Invalid Input(s). Please enter correct input(s).\n ")
            else:
                answerVCone= round(math.pi * (rad **2)* (height/3),2)
                print (f'The volume of a cone with a radius of {rad} and a height of {height} is {answerVCone}. ')
                break
        except:
                print ("Invalid Input(s). Please enter correct input(s).\n ")
    return True 

def SA_Cone():
    print('\033[1;32;40m\nWe will calculate the surface area of your cone!\nYou will need to input 2 positive values\nfor the radius of the base, and height.')
    while True: 
        rad= input("Please input the radius of the base, it must be a positive number: ").lower().replace(' ','')
        if rad=='quit':
            return False
        height=input("Please input the height of the cone: ").lower().replace(' ','')
        if height=='quit':
            return False
        try:
            rad=float(rad)
            height=float(height)
            if rad <= 0 or height <= 0: 
                print ("Invalid Input(s). Please enter valid value(s).\n ")
            else:
                answerSACone= (math.pi*rad**2)+math.sqrt(rad**2 + height **2)*rad*math.pi
                answerSACone=round(answerSACone,2)
                print (f'The surface area of a cone with a radius of {rad} and a height of {height} is {answerSACone}.')
                
                break
        except:
                print ("Invalid Input(s). Please enter valid number(s).\n ")
    return True 

def SA_cube():
    print('\033[1;36;40m\nWe will calculate the surface area of your cube! \n')
    while True: 
        side= input("Please input your side, it must be a positive number: ").lower().replace(' ','')
        if side=='quit':
            return False
        try:
            side=float(side)
            if side <= 0: 
                print ("Invalid Input. Please enter valid value.\n ")
            else:
                answerSAC= 6 * side **2
                print (f'\nThe surface area of a cube with a side length of {side} is {answerSAC}.')
                break
        except:
                print ("Invalid Input. Please enter valid number\n ")
    return True 

def SA_RecPrism():
    print('\033[1;37;40m\nWe will calculate the surface area of a rectangular prism.\nYou will need to input 3 positive values for the length,\nwidth, and height:')
    while True:
        l=input('What is the length of your prism?\n').lower().replace(' ','')
        if l=='quit':
            return False
        w=input('What is the width of your prism?\n').lower().replace(' ','')
        if w=='quit':
            return False
        h=input('What is the height of your prism?\n').lower().replace(' ','')
        if h=='quit':
            return False
        try:
            l=float(l)
            w=float(w)
            h=float(h)
            if l<=0 or w<=0 or h<=0:
                print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.\n')
            else:
                answerSAP=2 * (l*w+l*h+w*h)
                answerSAP=round(answerSAP,2)
                print(f'The surface area of a rectangular prism with side lengths {l}, {w}, and {h} is {answerSAP}\n')
                break
        except:
            print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.\n')
    return True 

def SA_Sphere():
    print('\033[1;35;40m\nWe will calculate the surface area of a sphere.\nYou will need to input 1 positive value for the radius.\n')
    while True: 
        rad= input("Please input your radius, it must be a positive value: ")
        rad=rad.lower().replace(' ','')
        if rad=='quit':
            return False
        try:
            rad=float(rad)
            if rad <= 0: 
                print ("Invalid Input. Please enter valid input.\n")
            else:
                answerSAS= 4 * math.pi* (rad ** 2)
                answerSAS=round(answerSAS,2)
                print (f'\nThe surface area of a sphere with radius {rad} is {answerSAS}')
                break
        except:
            print ("Invalid Input. Please enter valid input.\n")
    return True

def PyTheorem():
    print('\033[1;33;40m\nWe will find the missing side length of a right\ntriangle using the pythagorean theorem. You\nmust input 2 positive values.\n')
    while True:
        length=input('Are you looking for the hypotenuse, which is\nthe side opposite to the right angle? Yes/No: ')
        length=length.lower().replace(' ','')
        if length=='quit':
            return False
        if length=='yes':
            side1=input('\nWhat is the first side length: ').lower().replace(' ','')
            if side1=='quit':
                return False
            side2=input('\nWhat is the second side length: ').lower().replace(' ','')
            if side2=='quit':
                return False
            try:
                side1=float(side1)
                side2=float(side2)
                if side1<=0 or side2<=0:
                    print ("\nInvalid Input(s). Please enter valid input: ")
                else:
                    hyp= round(math.sqrt(side1**2+side2**2),2)
                    print(f'\nThe hypotenuse of a triangle with known side lengths of {side1} and {side2} is {hyp}.\n')
                return True
            except:
                print('Invalid inputs')

        elif length=='no':
            hyp=input('\nWhat is the hypotenuse length: ').lower().replace(' ','')
            if hyp=='quit':
                return False
            side1=input('\nWhat is the known side length: ').lower().replace(' ','')
            if side2=='quit':
                return False
            try:
                hyp=float(hyp)
                side1=float(side1)
                if side1>0 and hyp>side1:
                    side2=round(math.sqrt(hyp**2-side1**2),2)
                    print(f'\nThe missing side length of a triangle with known side of {side1} and hypotenuse of {hyp} is {side2}.')
                    return True
                else: 
                    print ("\nInvalid Input(s). Please enter valid input.")
            except:
                print('\nInvalid input(s).')
        else:
            print('Invalid answer, you must input either yes or no.\n')

def main():
    """
    main block of code that will run your program and control program flow
    You will need to include a while loop to keep repeating the commands until
    the user chooses to exit
    """
    x=True
    title()
    x=instructions()
    while x==True: 
        choice=start()
        if choice=='quit':
            break
        else:
            functionList=('nil',Vsphere,Vcube,VrecPri,Vcone,SA_Sphere,SA_cube,SA_RecPrism,SA_Cone,PyTheorem)
            x=functionList[choice]()
            


if __name__ == "__main__":
    main()

