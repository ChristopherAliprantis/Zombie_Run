import turtle
import random
import time

global zx, zy

def psetup():
    turtle.penup()
    turtle.goto(0, 0)
    global px, py
    px = turtle.xcor()
    py = turtle.ycor()

def spawn_zombie():
    global zx, zy
    turtle.pendown()
    turtle.color('green')
    turtle.penup()
    turtle.goto(random.randint(-850, 850), random.randint(-450, 450))
    turtle.pendown()
    turtle.dot(36)
    turtle.penup()
    turtle.color('black')
    zx = turtle.xcor()
    zy = turtle.ycor()

def zmove():
    global zx, zy
    while True:
        turtle.penup()
        turtle.setx(zx)
        turtle.sety(zy)
        time.sleep(0.1)
        turtle.color('green')
        support = random.randint(1, 4) # this is so the zombie has more acurate tracking, by having a thing to confirm it
        if py > zy and support ==1 :          
            zy=zy + 30
            turtle.pendown()
            turtle.color('white')
            turtle.dot(36)
            turtle.color('green')
            turtle.penup()
            turtle.sety(zy)
            turtle.pendown()
            turtle.dot(36)
            pmove()
        elif px > zx and support ==2:
            zx=zx + 30
            turtle.pendown()
            turtle.color('white')
            turtle.dot(36)
            turtle.color('green')
            turtle.penup()
            turtle.setx(zx)
            turtle.pendown()
            turtle.dot(36)
            pmove()
        elif px < zx and support ==3:
            zx=zx - 30
            turtle.pendown()
            turtle.color('white')
            turtle.dot(36)
            turtle.color('green')
            turtle.penup()
            turtle.setx(zx)
            turtle.pendown()
            turtle.dot(36)
            pmove()
        elif py < zy and support ==4:
            zy=zy - 30
            turtle.pendown()
            turtle.color('white')
            turtle.dot(36)
            turtle.color('green')
            turtle.penup()
            turtle.sety(zy)  
            turtle.pendown()
            turtle.dot(36)
            pmove()
        
def pmove():
    global py, px
    time.sleep(0.1)
    turtle.penup()
    turtle.setx(px)
    turtle.sety(py)
    turtle.color('black')
    if abs(px - zx) < 16 and abs(py - zy) < 16:
        print('You lost, the zombie ate you!')
        exit()
    print('move: w, a, s, d')
    pdir = input()
    if pdir=='w':    
        py=py + 30
        turtle.pendown()
        turtle.color('white')
        turtle.dot(36)
        turtle.color('black')
        turtle.penup()
        turtle.sety(py)
        turtle.pendown()
        turtle.dot(36)
    elif pdir=='d':
         px=px + 30
         turtle.pendown()
         turtle.color('white')
         turtle.dot(36)
         turtle.color('black')
         turtle.penup()
         turtle.setx(px)
         turtle.pendown()
         turtle.dot(36)
    elif pdir=='a':
         px=px - 30
         turtle.pendown()
         turtle.color('white')
         turtle.dot(36)
         turtle.color('black')
         turtle.penup()
         turtle.setx(px)
         turtle.pendown()
         turtle.dot(36)
    elif pdir=='s':
        py=py - 30
        turtle.pendown()
        turtle.color('white')
        turtle.dot(36)
        turtle.color('black')
        turtle.penup()
        turtle.sety(py)
        turtle.pendown()
        turtle.dot(36)
    else:
        print('Not a valid control enter a valid control next time!')
    if abs(px - zx) < 16 and abs(py - zy) < 16:
        print('You lost, the zombie ate you!')
        exit()
    time.sleep(0.1)        
    zmove()

turtle.dot(36)
spawn_zombie()
psetup()
pmove()