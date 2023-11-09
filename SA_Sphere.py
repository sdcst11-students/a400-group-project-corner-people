#!python3
#sphere (variables:Radius) (Formula:4piR^2)
import math
def SA_Sphere():
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
SA_Sphere()