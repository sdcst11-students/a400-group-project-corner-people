#!python3
    # Will display a title screen
    # input parameters: none needed
    # output parameters: None
    # Author: Copper
    # Modified:
    # title

def title():
    titlePage='\033[1;32m\n\nKimby\'s Python Calculator\n   By: Ruby and Kimmie\n Calculates:'
    calculators='\033[1;34m\nVolume,\nSurface Area,\nAnd More!'
    print(titlePage,calculators)
    return None

title()