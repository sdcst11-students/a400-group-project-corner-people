#!python3

def instructions():
   while True:
      instructions = input("Do you want the instructions? yes or no: ").lower().replace(" ", "")
      
      if instructions == "no":
         print ("Alright, lets go!")
         break 
      elif instructions== "yes":
         print ("These are the instructions! The program will ask you what you want to calculate\nThen, it will ask you the inputs needed.\nLet's Go! ")
         break 
      else: 
         print ("Invalid input. Please enter yes or no")
                 
instructions()
                  

