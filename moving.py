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
    radvalue = math.atan2(my - HH, mx - HW)
    return radvalue
def calc_distance(radians, mx, my):
    disvalue = math.hypot(mx-HW, my-HH)
    return int(disvalue)
def calc_x_direction(radians):
    x = math.cos(radians) * speed
    return x
def calc_y_direction(radians):
    y = math.sin(radians) * speed
    return y
def draw_circle_big():
    pygame.draw.circle(screen,WHITE,(int(x),int(y)), 25)
def draw_circle_small(x, y):
    pygame.draw.circle(screen, RED, (x, y), 5)
def quit():
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

