#!python3
import math 
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

Vsphere()
