#character description functions
def blade_light():
  print("Blade Light")
  print("Blade light is a low level enemy who should be fairly easy to defeat")
  print("Use your attacks wisely as these only regenerate each level")
  global bl_health ==  100




#/END CHARACTER FUNCTION\
#Main Character Variables
global mc_roundhousekick = 2



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
print("You continue to the next Village")
print("Welcome to village 2")
print("Here you find that there is a little bit more of civilisation")
print("You also can choose different paths here")
choice1 = input("To your right, you continue a little deeper in to the village, or to the left, there is a forest. No matter which way you go there is always the possibility you run in to an enemy")
if choice1 == right:
  print("Welcome to the village market")
  print("There is a enemy hiding somewhere, your challenge is to find them and defeat them")
  print("You could either walk around and find them, or wait for them to find you")
  choice2 = input("Enter 'wait' or 'walkaround'"):
  if choice2 == "wait":
    print("You wait around for a while and there is no sign of the enemy, you continue")
  if choice2 == "walkaround":
    print("You find the monster, he catches you by surprise and you have no time to attack, you die")
  

