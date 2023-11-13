#!python3
#sphere (variables:Radius) (Formula:4piR^2)
import math
def SA_Sphere():
    print('We will calculate the surface area of a sphere.\nYou will need to input 1 positive value for the radius.')
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