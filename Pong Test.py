import pygame as py

py.init()
RED = (255, 0, 0)
WHITE = (255,255,255)
BLUE = (0,0,254)
width = 1000
height = 1000
screen = py.display.set_mode([width,height])
rectx = 490
recty = 500
clock = py.time.Clock()

#create paddle objects
p1x = 925
p1y = 400
p2x = 50
p2y = 400
p1 = py.Rect(p1x-100,p1y,150,200)
p2 = py.Rect(p2x,p2y,25,200)

run = True
ballrect = py.Rect((rectx,recty),(50,50))
screen.fill(RED)
while run == True:
     screen.fill(WHITE)

     #draw ball
     py.draw.rect(screen, RED, ballrect)
     #move ball
     ballrect.x += 1



     keys = py.key.get_pressed()
     print("reached keys")
     if keys[py.K_DOWN]:
         if p1.y < 780:
             p1.y += 20
     if keys[py.K_UP]:
         if p1.y > 100:
             p1.y -= 20
     if keys[py.K_w]:
         if p2.y > 100:
             p2.y -= 20
     if keys[py.K_s]:
         if p2.y < 780:
             p2.y += 20

     # draw paddles
     py.draw.rect(screen, RED, p1)  # right paddle
     py.draw.rect(screen, RED, p2)  # left paddle



     py.display.update()
     clock.tick(60)



