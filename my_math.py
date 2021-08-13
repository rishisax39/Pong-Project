import math 

def calcSpeedX(angle,speed):
     speedX = math.cos(angle) * speed
     return speedX
    

def calcSpeedY(angle,speed):
     speedX = math.sin(angle) * speed
     return speedX

def doesIntersect(circleRadius, circleX, cicrleY, rectX,rectY,rectLenght, rectWidth):
  pass 



assert calcSpeedX(angle=0,speed=1) == 1

assert calcSpeedX(angle=0,speed=5) == 5






print("File finished running")
