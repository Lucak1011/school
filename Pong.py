import pygame
from pygame.locals import *
pygame.init

##-------------------------------------//Variables//-------------------------------------##
x = 470
xspeed = 5
y = 260
yspeed = 5

enemyx = 940
enemyy = 0

playerx = 10
playery = 220

delay = 25

##-------------------------------------//Creating Window//-------------------------------------##

####--------------------------------------------------------------------------------------------------------------------------------------------------------------------####
####------------------------------------------------------------------/////DO NOT ALTER THE BELOW/////------------------------------------------------------------------####
window = pygame.display.set_mode((960,540))


running = True
while running == True:
    pygame.time.delay(delay)
    # This will repeat


    # checks if x button is pressed to quit the game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
####------------------------------------------------------------------/////DO NOT ALTER THE ABOVE/////------------------------------------------------------------------####
####--------------------------------------------------------------------------------------------------------------------------------------------------------------------#### 
            
##-------------------------------------//Creating Objects//-------------------------------------##
    
#--------------------------------/The Ball/--------------------------------#
    window.fill((0,0,0))
    pygame.draw.rect(window, (255,255,255), (x,y,20,20))
    x = x + xspeed
    y = y + yspeed

    if (x > 940):
        xspeed = 0
        yspeed = 0
    if (5 > x):
        xspeed = 0
        yspeed = 0
    if (y > 520):
        yspeed = -yspeed
    if (0 > y):
        yspeed = -yspeed

#--------------------------------/Enemy Pad/--------------------------------#
    pygame.draw.rect(window, (255,0,0), (enemyx, enemyy, 10, 100))
    enemyy = y - 50
#--------------------------------//Pad Collision//--------------------------------#
    if(y > enemyy and y < enemyy + 100):
        if(x > enemyx - 20):
            xspeed = -xspeed
    
#--------------------------------/Player Pad/--------------------------------#
    pygame.draw.rect(window, (0,0,255), (playerx, playery, 10, 100))
    
    if(y > playery and y > playery - 100):
        if(x == playerx + 10):
            xspeed = -xspeed
    
##-------------------------------------//Keybinds//-------------------------------------##

    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        playery = playery - 5
        
    keys = pygame.key.get_pressed()
    if keys[K_DOWN]:
        playery = playery + 5

####----------------------------------------------------------------------/////END OF SCRIPT/////----------------------------------------------------------------------####
        
    pygame.display.update() #updates screen
pygame.quit()
