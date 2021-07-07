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
speed = 3

def get_mouse_pos():
    x, y = pygame.mouse.get_pos()
    return x, y
def calc_radians (HW, HH, my, mx):
    """
    Calculate the distance between 2 points
    XXX: You're using argument names that are the variables of how you use this function, but that doesn't have to be so. 
        Instead, I suggest dissoaciating the argument names from how they're removed for readability.  I.E use (x1, y1, x2, y2) 
    """
    radvalue = math.atan2(my - HH, mx - HW)
    return radvalue
def calc_distance(radians, mx, my):
    """
    Calculates the distance between two points. 
    XXX: The arguments should actually be (x1, y1, x2, y2)
    """
    disvalue = math.hypot(mx-HW, my-HH)
    return int(disvalue)
def calc_x_direction(radians):
    """
    Calculates the x-delta traveling "distance" at the specified angle
    XXX: arguments should be (distance, radians), and use distance instead of speed so this function is pure.  
    """
    x = math.cos(radians) * speed
    return x
def calc_y_direction(radians):
    """
    Calculates the y-delta traveling "distance" at the specified angle
    XXX: same as above
    """
    y = math.sin(radians) * speed
    return y
def draw_circle_big():
    """
    Draws a circle on the screen.  
    XXX: 
        Make this into a "pure" and reusable function by taking arguments to describe the circle. 
        Example function signature draw_circle(centerx,centery,radius,color).  
        Then you can use this instead of "draw_circle_small"
    """
    pygame.draw.circle(screen,WHITE,(int(x),int(y)), 25)
def draw_circle_small(x, y):
    """
    Draws a small circle
    XXX: I think this function can be removed. 
    """
    pygame.draw.circle(screen, RED, (x, y), 5)
    
def quit():
    """
    Quit's the window if certain keys are pressed
    XXX: Make this function reusable by taking in the keys that should be pressed. 
    XXX: doesn't work
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            pygame.quit()
            sys.exit()
     
while flag == True:
     # quit()
     screen.fill(BLACK)
     for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = get_mouse_pos()
            radians = calc_radians(HW, HH, my, mx)
            print(radians)
            distance = calc_distance(radians, mx, my)
            dx = calc_x_direction(radians)
            dy = calc_y_direction(radians)
            draw_circle_small(mx, my)
            print("click")




     if distance > 0:
         distance -= 1
         x += dx
         y += dy
         draw_circle_big()





     clock.tick(120)
     pygame.display.update()

