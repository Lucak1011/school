
'''
Some of these things kinda work. Some don't. Didn't have the time to do as much as I wanted to.
In the top bar of this file, there is a download button, it will download as a python file, you can either drag and drop it into the virtualbox files folder OR open it in notepad.

'''


#inputty stuff
from random import randint

#character description functions
def blade_light():
  print("Blade Light")
  print("Blade light is a low level enemy who should be fairly easy to defeat")
  print("Use your attacks wisely as these only regenerate each level")
  global bl_health
  bl_health = 100

def pepsiman():
    print("You meet pepsi man")
    reply = input("Do you reply to Pepsi Man, Y or N")
    if reply == "Y":
        print("Pepsi Man gives you a magic key")
        global magic_key
        magic_key = True
    else:
        print("Pepsi man explodes and you die")
def colonel_sanders():
    print("Welcome to KFC Land lad")
    print("Answer the next 3 questions correctly to proceed")

def harry_potter():
  print("Harry Potter has arrived")
  print("You must defeat Albus Dumbledore to pass")
  print("He has a power level of 9")


#/END CHARACTER FUNCTION\
#Main Character Variables
global mc_roundhousekick

mc_roundhousekick = 2



print("Welcome to_____")
print("Within this game you must proceed through several villages of increasing difficulty")
print("You will also face several enemies, also of increasing difficulty")
print("At some point in a village which shall not be named, you will unlock a shop")
print("This shop will allow you to buy, sell and upgrade your weapons/tools")
print("You start with a basic sword and a basic axe")
print("The sword can be used to attack people and the axe can be used to break down doors")

#village 1
print("You are now in village 1")
print("This village is calm and quiet, there is only one option and that is to continue straight, be careful")
blade_light()
print("To use roundhoues kick: type rhk")
print("To attack using your sword: type 'sword'")
blattack = True
while blattack == True:
  am = input("Enter attack method")
  if am == "rhk":
    print("You roundhouse kick Blade Light, his health drops by 20")
    bl_health = bl_health - 20
    if bl_health == 0:
      blattack = False
  if am == "sword":
    print("You stab Blade Light")
    print("His health drops by ten")
    bl_health = bl_health - 10
    if bl_health == 0:
      blattack = False
print("Village 1 complete")
  
#village 2
print("Welcome to village two")
path = input("You can go L or R")
if path == "L":
    pepsiman()
    print("You then get attacked by an evil gremlin")
    print("You are now dead")

if path == "R":
    print("You go right")
    colonel_sanders()
    q1 = input("What is KFC's slogan")
    if q1 == "finger lickin good":
        print("Correct")
        q2 = input("Who is Colenol Sanders?")
        if q2 == "KFC man":
          print("Correct - proceed.")
          q3 = input("Is Rayhan Rayhan?")
          if q3 == "Y":
            print("Correct, proceed")
            print("You completed the village, well done")
            print("Welcome to the third village (Village 3) ")
            
            print("In this village - you will recieve a screwdriver")
            global screwdriver
            screwdriver = 1
            print("You have the option if going Left or heading towards an abandoned house")
            dir = input("House or Left")
            if dir == "Left":
              print("You exit the village safely")
            elif dir == "House":
              print("Welcome to the abandoned house")
              print("There is a 50 50 chance of being able to successfully enter the house")
              n1 = randint(1,2)
              print("You try the screwdriver on the lock")
              if n1 == 1:
                print("Welcome to the house.")
                screwdriver = 0 
                print("There is a staircase that goes to the basement? Do you go down it?")
                dir = input("Do you go down the staircase? Y or N")
                if dir == "N":
                  print("You continue throught the house, there is a man, do you speak to the man?")
                  ans = input("Do you speak to the man, Y or N")
                  if ans == "Y":
                    print("The man decides he wants to give you a tenner, enjoy")
                    print("Carry on")
                    print("You meet a man who is called Rick")
                    print("Rick makes a pledge to you:")
                    print("Rick will never give you up")
                    print("He will never let you down")
                    print("He will never turn around and desert you")
                                
              
              else:
                print("Death, the door shoots you for breaking and entering (B&E)")
            
    
    else:
        print("Wrong. Bye bye")
