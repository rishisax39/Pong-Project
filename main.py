import pygame as py
import sys
sys.version
py.init()

# VARIABLES
LIGHTRED = (255, 100, 100)
WHITE = (255,255,255)
BLUE = (0,0,255)
width = 1000
height = 1000
screen = py.display.set_mode((width,height), flags = True, vsync = 1)
scorep1 = 0
scorep2 = 0
py.display.set_caption("Pong")
clock = py.time.Clock()

vel = 20
run = True
bx = 490
by = 500
rectx = 490
recty = 500
br = 20
playing = False

class Ball:
    def __init__ (self,screen,color,posX,posY,radius): #construct ball object
        self.screen = screen
        self.color = color
        self.posX = posX
        self.posY = posY
        self.radius = radius
        self.dx = 0
        self.dy = 0
        self.show()
    def start_moving(self):  #start moving ball by adding values to direction variables
        self.dx = 0
        self.dy = -5
    def move_ball(self):     #move ball by changing position coordinates of ball
        self.posX = self.posX + self.dx
        self.posY = self.posY + self.dy
    def show(self):
        py.draw.circle(self.screen, self.color, (self.posX, self.posY), self.radius)

    def collisionTopWall(self):
        print("reached top wall")

        self.dy *= -1

    def collisionBottomWall(self):
        pass

class Paddle:
    def __init__(self,display, color, posX, posY, width, height):
        self.color = color
        self.posX = posX
        self.posY = posY
        self.screen = screen
        self.width = width
        self.height = height

    def displayOnScreen(self):
        py.draw.rect(self.screen, self.color,(self.posX, self.posY, self.width, self.height))

    def movePaddle1Down(self):
        keys = py.key.get_pressed()
        if keys[py.K_DOWN]:
            self.posY += 20


    def movePaddle1Up(self):
        keys = py.key.get_pressed()
        if keys[py.K_UP]:
            self.posY -= 20

    def movePaddle2Down(self):
        keys = py.key.get_pressed()
        if keys[py.K_s]:
            p2.posY += 20

    def movePaddle2Up(self):
        keys = py.key.get_pressed()
        if keys[py.K_w]:
            p2.posY -= 20







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




# create ball object
ball = Ball(screen, WHITE, width//2, height//2,15 )

# create paddle object
p1 = Paddle(screen,WHITE,925,400, 25, 150)
p2 = Paddle(screen,WHITE,100,400, 25, 150)





while run == True:
    screen.fill(LIGHTRED)
    redraw_score()
    # drawing paddle 1 (right side)
    p1.displayOnScreen()
    # drawing paddle 2 (left side)
    p2.displayOnScreen()

    for event in py.event.get():
        if event.type == py.QUIT:
            print("reached")
            py.quit()
    ball.start_moving()
    ball.move_ball()
    ball.show()

    # paddle movement up and down algorithm
    if p1.posY < 840:
        p1.movePaddle1Down()
    if p1.posY > 100:
        p1.movePaddle1Up()
    if p2.posY < 840:
        p2.movePaddle2Down()
    if p2.posY > 100:
        p2.movePaddle2Up()

    # detect collision with top wall
    if ball.posY <= 100:
        print("reached collis")
        ball.collisionTopWall()


    # draw score bar
    py.draw.rect(screen,WHITE,(0,100,1000,15))

    py.display.flip()
    clock.tick(60)


py.quit()
