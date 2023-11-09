#!python3
def SA_cube():
    while True: 
        side= input("Please input your side, it must be a positive number: ")
        try:
            side=float(side)
            if side <= 0: 
                print ("Invalid Input. Please enter correct input: ")
            else:
                answerSAC= 6 * side **2
                print (f'The surface area of a cube with a side of {side} is {answerSAC}')
                break
        except:
                print ("Invalid Input. Please enter correct input: ")


SA_cube()
