#!python3
def SA_cube():
    print('We will calculate the surface area of a cube.\nYou will need to input 1 positive value for the side length.')
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


SA_cube()
