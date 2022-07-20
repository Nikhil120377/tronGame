from turtle import *
from random import *
from base import *

p1 =Vector(-100,0)
p1Aim = Vector(4,0)
p1body = set()

p2 =Vector(100,0)
p2Aim = Vector(-4,0)
p2body = set()


def inside(head):
    return -200<head.x<200 and -200<head.y<200

def move():
    p1.move(p1Aim)
    p1head = p1.__copy__()

    p2.move(p2Aim)
    p2head = p2.__copy__()

    if not inside(p1head) or p1head in p2body:
        print("player blue has won")
        return

    if not inside(p2head) or p2head in p1body:
        print("player red has won")
        return

    p1body.add(p1head)
    p2body.add(p2head)

    square(p1.x,p1.y,3,'red')
    square(p2.x, p2.y, 3, 'blue')
    ontimer(move,50)





setup(420,420,370,0)
hideturtle()
tracer(False)
listen()
onkey(lambda : p1Aim.rotate(90),'w')
onkey(lambda : p1Aim.rotate(-90),'s')
onkey(lambda : p2Aim.rotate(90),'Up')
onkey(lambda : p2Aim.rotate(-90),'Down')
move()
done()
