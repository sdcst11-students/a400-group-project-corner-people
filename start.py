#!python3
#Lists the different functions available
# Asks what user would like to calculate
#Runs specific command
'''
Volume calculations 
Sphere: ( variables: radius formula:4/3pir^3)
Cube: (variables: side formula: s^3)
Rectangular prism (variables: l W H, formula: LWH)
Cone: (variable: base, height formula: BH)
SA Calculations 
sphere (variables:Radius) (Formula:4piR^2)
Cube (Variables:Side Length) (Formula:6S^2)
Rectangular prism (v:length,width,height) (F:2 lw+lh+hw)
Cone (v:radius, height)(F:piR^2+pi(sqrt(rad^2+height^2))(rad)
Phythereom formula 
	(variables: Side a, Side b, side c, Which side calculating)(a^2+b^2=c^2)
'''
def start():
    while True:
        Ins='Type a number to commence the specific function.\n:'
        VC='\n  Volume Calculations:\n           Sphere==>1\n             Cube==>2\nRectangular Prism==>3\n             Cone==>4'
        SAC='\n\nSurface Area Calculations:\n               Sphere==>5\n                 Cube==>6\n    Rectangular Prism==>7\n                 Cone==>8'
        PT='\n\nPythagorean Theorem==>9\n'
        TotalInstructions=VC+SAC+PT+Ins

        choice=input(TotalInstructions)
        try:
            choice=int(choice)
            if 0<choice<=9:
                return choice
            else:
                print('Invalid input\nYou must input an integer between 1 and 9.\n')
        except:
            print('Invalid input\nYou must input an integer between 1 and 9.\n')
choice=start()