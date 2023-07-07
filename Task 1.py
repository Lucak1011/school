import pygame
from pygame.locals import*
pygame.init()

# /// DO NOT CHANGE THE BELOW \\\ #     
window = pygame.display.set_mode((800,500))
x = 0
y = 0
delay = 50
enemyx = 780
enemyy = 0 
xspeed = 5
yspeed = 1

playerx = 20
playery = 200
playerspeed = 5

# /// DO NOT CHANGE THE ABOVE \\\ #

running = True
while running == True:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # /// the ball \\\ # 
    window.fill((255,0,0))
    pygame.draw.rect(window, (120, 200, 255), (x, y, 20, 20))
    x = x + xspeed
    y = y + yspeed
    # /// above is the ball \\\ # 

    # /// The Pad \\\ # 
    pygame.draw.rect (window, (120, 200, 255), (enemyx, enemyy, 10, 100))
    enemyy = y - 50

    # /// E Pad collisions \\\ #
    if (y > enemyy and y < enemyy + 100):
        if (x > enemyx - 20):
            xspeed = -xspeed

    #/// The Player pad \\\#
    pygame.draw.rect(window,(120,200,255),(playerx,playery,20,100))
    #/// collision \\\#

    if(y > playerx and y < playery + 100):
        xspeed = -xspeed

    # /// Above is The Pad \\\ #

    if (x > 780):
        xspeed = -xspeed
    if (x < 0):
        xspeed = -xspeed
    if (y > 480):
        yspeed = -yspeed
    if (y < 0):
        yspeed = -yspeed

# /// KEYBINDS \\\ #
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        playery = playery - playerspeed
        
    keys = pygame.key.get_pressed()
    if keys[K_DOWN]:
        playery = playery + playerspeed
        
    pygame.display.update()

pygame.quit()
