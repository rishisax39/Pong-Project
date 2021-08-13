import pygame
import math
import sys
import random
flag = True
W,H = 1920, 1080
dx,dy = 0,0
distance = 0

# define colors
RED = (255,0,0)
WHITE = (255,255,255)
BLACK = (0,0,0)

# initialize display
pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((W,H))
HW = W/2
HH = H/2
x,y = HW, HH


def get_mouse_pos():
    x, y = pygame.mouse.get_pos()
    return x, y
def calc_radians (x1, y1, x2, y2):
    """
    Calculate the distance between 2 points
    XXX: You're using argument names that are the variables of how you use this function, but that doesn't have to be so. 
        Instead, I suggest dissoaciating the argument names from how they're removed for readability.  I.E use (x1, y1, x2, y2) 
    """
    radvalue = math.atan2(y2 - y1, x2 - x1)
    return radvalue
def calc_distance(x1, y1, x2, y2):
    """
    Calculates the distance between two points. 
    XXX: The arguments should actually be (x1, y1, x2, y2)
    """
    disvalue = math.hypot(x2-x1, y2-y1)
    return int(disvalue)
def calc_x_direction(speed, radians):
    """
    Calculates the x-delta traveling "distance" at the specified angle
    XXX: arguments should be (distance, radians), and use distance instead of speed so this function is pure.  
    """
    x = math.cos(radians) * speed
    return x
def calc_y_direction(speed, radians):
    """
    Calculates the y-delta traveling "distance" at the specified angle
    XXX: same as above
    """
    y = math.sin(radians) * speed
    return y
def draw_circle(surface,COLOR,center,radius):
    """
    Draws a circle on the screen.  
    XXX: 
        Make this into a "pure" and reusable function by taking arguments to describe the circle. 
        Example function signature draw_circle(centerx,centery,radius,color).  
        Then you can use this instead of "draw_circle_small"
    """
    pygame.draw.circle(surface,COLOR,center,radius)
def quit(QUIT, DOWN, ESCAPE):
    """
    Quit's the window if certain keys are pressed
    XXX: Make this function reusable by taking in the keys that should be pressed. 
    XXX: doesn't work
    """
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == DOWN and event.key == ESCAPE):
            pygame.quit()
            sys.exit()

while flag == True:
    quit(pygame.QUIT, pygame.KEYDOWN, pygame.K_ESCAPE)
    screen.fill(BLACK)

    mx, my = get_mouse_pos()
    radians = calc_radians(x, y, mx, my)
    print(radians)
    distance = calc_distance(HW, HH, mx, my)
    dx = calc_x_direction(3, radians)
    dy = calc_y_direction(3, radians)
    print("click")
    x += dx
    y += dy
    sx, sy = get_mouse_pos()
    smallcenter = (sx, sy)
    bigcenter = (int(x), int(y))
    draw_circle(screen, RED, smallcenter, 5)
    draw_circle(screen, WHITE, bigcenter, 25)




    clock.tick(120)
    pygame.display.update()

