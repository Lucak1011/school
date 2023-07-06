import pygame
from pygame.locals import*
pygame.init()

# /// DO NOT CHANGE THE BELOW \\\ #     
window = pygame.display.set_mode((800,500))
x = 0
y = 0
delay = 50

xspeed = 5
yspeed = 1

# /// DO NOT CHANGE THE ABOVE \\\ #

running = True
while running == True:
    pygame.time.delay(delay)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    window.fill((255,0,0))
    pygame.draw.rect(window, (120, 200, 255), (x, y, 20, 20))
    x = x + xspeed
    y = y + yspeed

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
        delay = delay + 5

    if keys[K_DOWN]:
        delay = delay - 5
        
    pygame.display.update()

pygame.quit()
