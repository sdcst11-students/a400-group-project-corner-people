#!python3
#Rectangular prism (v:length,width,height) (F:2 lw+lh+hw)
def SA_RecPrism():
    print('We will calculate the surface area of a rectangular prism.\nYou will need to input 3 positive values for the length,\nwidth, and height:')
    while True:
        l=input('What is the length of your prism?\n')
        w=input('What is the width of your prism?\n')
        h=input('What is the height of your prism?\n')
        try:
            l=float(l)
            w=float(w)
            h=float(h)
            if l<=0 or w<=0 or h<=0:
                print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.')
                break
            answerSAP=2 * (l*w+l*h+w*h)
            print(f'The surface area of a rectangular prism with side lengths {l}, {w}, and {h} is {answerSAP}')
        except:
            print('Atleast one of your inputs is invalid.\nPlease input 3 positive numbers.')

SA_RecPrism()