
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

Vcube()
