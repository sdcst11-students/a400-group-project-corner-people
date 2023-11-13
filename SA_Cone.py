#!python3

#Cone (v:radius, height)(F:piR^2+pi(sqrt(rad^2+height^2))(rad)
import math
def SA_Cone():
    print('We will calculate the surface area of a cone.\nYou will need to input 2 positive values\nfor the radius of the base, and height.')
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
SA_Cone()