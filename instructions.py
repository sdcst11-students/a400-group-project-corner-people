#!python3
def instructions():
    intrustions= input("Would you like to see the instructions for this calculator? Yes or No")
    intrustions = strip(intrustions)
    if intrustions == "yes":
        instructions = "This is calculator can help you with diffcult solutions. \nYou can calculate the volume and surface area of these four shapes: Sphere, cube, rectangular prism, cone"
        print (instructions)
    else:
        pick: 