import pygame
import math
import sys
import random
flag = True

dx,dy = 0,0
distance = 0

# define colors
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)


# display surface
W = 1000
H = 1000
HW = W/2
HH = H/2

x,y = HW, HH
dx,dy = 0,0
pmx,pmy = x,y
dx,dy =0,0
distance = 0
speed = 3

# initialize display
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))

while flag == True:
    # quit game sequence
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # when mouse clicked
        if event.type == pygame.MOUSEBUTTONDOWN and not distance:
            print("reached click")
            # return position of mouse cursor and set to mx, my
            mx, my = pygame.mouse.get_pos()
            print(mx)
            radians = math.atan2(my-pmy, mx - pmx)
            # calc distance from cursor to circle, a^2 + b^2 = c^2
            distance = math.hypot(mx-pmx,my-pmy)/3
            distance = int(distance)

            # calc distance to travel x coordinate
            dx = math.cos(radians) * speed
            # calc distance to travel y coordinate
            dy = math.sin(radians) * speed

            pmx, pmy = mx, my
            # move white circle sequence
            if distance > 0:
                print("dx is: " + str(dx))
                print("dy is: " + str(dy))
                # adding direction to x y
                x += dx
                y += dy
                distance -= 1
                print("reached distance > 0")
            pygame.draw.circle(screen, WHITE, (int(x), int(y)), 25, 0)
            if distance > 0:
                pygame.draw.circle(screen, RED, (pmx, pmy), 5, 0)
                # print("reached distance " + str(distance))
    clock.tick(120)
    pygame.display.update()
    screen.fill(BLACK)

