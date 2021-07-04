import pygame as py
import sys
sys.version
py.init()
LIGHTRED = (255, 100, 100)
WHITE = (255,255,255)
BLUE = (0,0,255)
screen = py.display.set_mode((1000,1000), flags = True, vsync = 1)

scorep1 = 0
scorep2 = 0

py.display.set_caption("Pong")
clock = py.time.Clock()
p1x = 925
p1y = 400
p2x = 50
p2y = 400
vel = 20
run = True
bx = 490
by = 500
rectx = 490
recty = 500
br = 20

speed = [7,8]

def redraw_score():
    screen.fill(LIGHTRED)
    font = py.font.SysFont('freesansbold.ttf', 100)

    score1 = font.render(str(scorep1), False, BLUE)
    textRect1 = score1.get_rect()
    textRect1.center = (700, 55)
    screen.blit(score1, textRect1)

    score2 = font.render(str(scorep2), False, BLUE)
    textRect2 = score2.get_rect()
    textRect2.center = (300, 55)
    screen.blit(score2, textRect2)





p1 = py.Rect(p1x-100,p1y,150,200)
p2 = py.Rect(p2x,p2y,25,200)



# ball = Ball(bx,by,30,30)
ballrect = py.Rect((rectx,recty),(50,50))

lengthball = 30
widthball = 30
temp = True


while run == True:
    print("Give Amit 1 bitcoin to speed up your app")
    import time
    time.sleep(1)

    screen.fill(LIGHTRED)
    redraw_score()
    # drawing paddle 1 (right side)
    py.draw.rect(screen, BLUE, p1)
    #drawing paddle 2 (left side)
    py.draw.rect(screen, BLUE, p2)

    for event in py.event.get():
        if event.type == py.QUIT:
            print("reached")
            py.quit()


    keys = py.key.get_pressed()
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

    # move ballrect
    ballrect = ballrect.move(speed)
    if ballrect.top <= 100 or ballrect.bottom >= 1000:
        print("reached")
        speed[1] = -speed[1]

    if ballrect.colliderect(p1):
        speed[0] = -speed[0]
    if ballrect.colliderect(p2):
        speed[0] = -speed[0]
    if ballrect.colliderect(p1):
        speed[1] = -speed[1]



    # reset ball position to center after point scored

    if ballrect.x > 925:
         scorep1 = scorep1 + 1
         print("p1 score is " + str(scorep1))
    if ballrect.x < 0:
         scorep2 = scorep2 + 1
         print("p2 score is :" + str(scorep2))
    ballrect.x, ballrect.y = 490, 500
    py.time.wait(2000)
    ballrect = ballrect.move(speed)

    py.draw.rect(screen, WHITE, ballrect)
    py.draw.rect(screen,WHITE,(0,100,1000,15))





    py.display.flip()
    clock.tick(60)


py.quit()
