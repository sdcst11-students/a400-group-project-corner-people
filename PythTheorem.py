#!python3
#c=sqrt(a^2+b^2),  b=sqrt(c^2-a^2)
import math
def PyTheorem():
    print('We will find the missing side length of a right\ntriangle using the pythagorean theorem. You\nmust input 2 positive values.')
    while True:
        length=input('Are you looking for the hypotenuse, which is\nthe side opposite to the right angle? Yes/No: ')
        length=length.lower()
        length=length.replace(' ','')
        if length=='yes':
            while True:
                side1=input('What is the first side length: ')
                if TestValues(side1)==False:
                    break
                side1=float(side1)
                side2=input('What is the second side length: ')
                if TestValues(side2)==False:
                    break
                side2=float(side2)
                hyp=math.sqrt(side1**2+side2**2)
                print(f'The hypotenuse of a triangle with known side lengths of {side1} and {side2} is {hyp}.')
                break
        elif length=='no':
            while True:
                hyp=input('What is the hypotenuse length: ')
                if TestValues(hyp)==False:
                    break
                hyp=float(hyp)
                side1=input('What is the known side length: ')
                if TestValues(side1)==False:
                    break
                side1=float(side1)
                side2=math.sqrt(hyp**2-side1**2)
                print(f'The missing side length of a triangle with known side of {side1} and hypotenuse of {hyp} is {side2}.')
                break
        else:
            print('Invalid answer, you must input either yes or no.')

def TestValues(a):
    try:
        a=float(a)
        if a>0:
            return True
        else:
            print('That is not a valid input.')
            return False
    except:
        print('That is not a valid input.')
        return False
    
PyTheorem()