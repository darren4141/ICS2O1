'''
=====================================================================================================================================================================
Turtle graphics truck
DARREN LIU
1/25/2022
PYTHON VER 3.7.0
=====================================================================================================================================================================
PROBLEM DEFINITION: Draw a truck using turtle graphics
INPUT(N/A)
OUTPUT: truck and background
=====================================================================================================================================================================
'''

from turtle import *

t=Turtle()
s=Screen()
t.screen.bgcolor("midnight blue")
t.hideturtle()
t.speed(0)

def base():
    t.color("black")

    #horizontal bottom rectangle
    t.penup()
    t.goto(-400, -100)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.fd(600)
    t.setheading(90)
    t.fd(50)
    t.setheading(180)
    t.fd(600)
    t.setheading(270)
    t.fd(50)
    t.end_fill()

    #vertical right rectangle
    t.goto(200, -50)
    t.begin_fill()
    t.setheading(90)
    t.fd(150)
    t.setheading(180)
    t.fd(30)
    t.setheading(270)
    t.fd(150)
    t.end_fill()

def driver_seat():

    #driver seat
    t.color("goldenrod")
    t.penup()
    t.goto(200, -95)
    t.pendown()
    t.begin_fill()
    t.setheading(90)
    t.fd(195)
    t.setheading(75)
    t.fd(40)
    t.setheading(0)
    t.fd(140)
    t.setheading(300)
    t.fd(70)
    t.setheading(270)
    t.fd(173)
    t.end_fill()
    
def back_box():

    #base
    t.color("saddle brown")
    t.penup()
    t.goto(-330, -50)
    t.pendown
    t.begin_fill()
    t.setheading(160)
    t.fd(60)
    t.setheading(0)
    t.fd(500)
    t.setheading(200)
    t.fd(60)
    t.end_fill()

    #box
    t.color("goldenrod")
    t.penup()
    t.goto(-330, -50)
    t.setheading(160)
    t.fd(60)

    t.begin_fill()
    t.setheading(180)
    t.fd(40)
    t.setheading(0)
    t.fd(40)
    t.pendown()
    t.begin_fill()    
    t.fd(510)
    t.setheading(75)
    t.fd(200)

    t.fd(20)
    t.setheading(10)
    t.fd(70)
    t.setheading(85)
    t.fd(15)
    t.setheading(180)
    t.fd(130)
    t.setheading(255)
    t.fd(50)
    
    t.setheading(185)
    t.fd(600)
    t.setheading(290)
    t.fd(10)
    t.setheading(255)
    t.fd(100)
    t.setheading(330)
    t.fd(50)    
    
    t.end_fill()

def wheels(x,y):

    #tires
    t.color("gray10")
    t.setheading(0)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #wheel outer rim
    t.color("silver")
    t.penup()
    t.goto(x, y+14)
    t.pendown()
    t.begin_fill()
    t.circle(35)
    t.end_fill()
    
    
    #wheel inner dot
    t.color("gray")
    t.setheading(0)
    t.penup()
    t.goto(x, y+40)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()


    

def wheel_frames():
    t.color("gold1")
    t.pensize(10)

    #back wheel frames
    t.penup()
    t.goto(-360, -85)
    t.pendown()
    t.setheading(45)
    t.fd(40)
    t.setheading(0)
    t.fd(190)
    t.setheading(315)
    t.fd(40)

    #front wheel frames
    t.penup()
    t.goto(200, -85)
    t.pendown()
    t.setheading(45)
    t.fd(40)
    t.setheading(0)
    t.fd(70)
    t.setheading(315)
    t.fd(40)

    t.pensize(1)

def windows():

    #window
    t.color("cornflower blue")
    t.color("midnight blue")
    t.penup()
    t.goto(230, 40)
    t.pendown()
    t.begin_fill()
    t.setheading(90)
    t.fd(65)
    t.setheading(0)
    t.fd(110)
    t.setheading(290)
    t.fd(80)
    t.setheading(175)
    t.fd(110)
    t.end_fill()

    #seperator
    t.color("goldenrod")
    t.penup()
    t.goto(260, 130)
    t.pendown()
    t.begin_fill()
    t.setheading(270)
    t.fd(100)
    t.setheading(0)
    t.fd(10)
    t.setheading(90)
    t.fd(100)
    t.end_fill()

    #back window glare
    t.pensize(4)
    t.color("white")
    t.penup()
    t.goto(260, 130)
    t.setheading(250)
    t.fd(25)
    t.pendown()
    t.fd(70)
    t.setheading(358)
    t.penup()
    t.fd(10)
    t.pendown()
    t.setheading(70)
    t.fd(70)
    t.pensize(1)

    #front window glare
    t.pensize(4)
    t.penup()
    t.goto(335, 130)
    t.setheading(250)
    t.fd(27)
    t.pendown()
    t.fd(73)
    t.setheading(358)
    t.penup()
    t.fd(15)
    t.pendown()
    t.setheading(70)
    t.fd(70)
    t.pensize(1)

    #window frame()
    t.color("goldenrod")
    t.pensize(4)
    t.penup()
    t.goto(228, 38)
    t.pendown()
    t.setheading(90)
    t.fd(68)
    t.setheading(0)
    t.fd(112)
    t.setheading(290)
    t.fd(82)
    t.setheading(175)
    t.fd(112)
    t.pensize(1)

def headlights(x, y, length):
    #headlights
    t.color("orange red")
    for i in range(0, length):
        t.penup()
        t.goto(x-i, y-i/20)
        t.pendown()
        t.begin_fill()
        t.circle(10)
        t.end_fill()

def box_details(x,y, length):
    #box details (parallelogram)
    t.color("gold1")
    t.penup()
    t.goto(x, y)
    t.begin_fill()
    t.setheading(75)
    t.fd(length)
    t.setheading(5)
    t.fd(30)
    t.setheading(255)
    t.fd(length+3)
    t.setheading(180)
    t.fd(30)
    t.end_fill()

def dirt():
    #dirt inside the truck
    t.color("saddle brown")
    t.penup()
    t.goto(-360, 120)
    t.pendown()
    t.begin_fill()
    t.setheading(30)
    t.fd(70)
    t.setheading(60)
    t.fd(40)
    t.setheading(0)
    t.fd(70)
    t.setheading(345)
    t.fd(50)
    t.setheading(15)
    t.fd(40)
    t.setheading(20)
    t.fd(65)
    t.setheading(330)
    t.fd(50)
    t.setheading(30)
    t.fd(30)
    t.setheading(330)
    t.fd(50)
    t.setheading(300)
    t.fd(50)
    t.end_fill()

def ground():
    #pavement
    t.color("dim gray")
    t.penup()
    t.goto(-1000, -160)
    t.pendown()
    t.begin_fill()
    t.setheading(0)
    t.fd(2000)
    t.setheading(270)
    t.fd(500)
    t.setheading(180)
    t.fd(2000)
    t.end_fill()

def building(x, y, width, height):
    
    #building
    t.color("dark gray")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.setheading(90)
    t.fd(height)
    t.setheading(0)
    t.fd(width)
    t.setheading(270)
    t.fd(height)
    t.setheading(180)
    t.fd(width)
    t.end_fill()

    #windows
    t.color("light yellow")
    for i in range(0, width//40):
        for j in range(0, height//40):
            t.penup()
            t.goto(x +10 + i*40, y + 10 + j*40)
            t.pendown()

            t.begin_fill()
            t.setheading(0)
            t.fd(20)
            t.setheading(90)
            t.fd(20)
            t.setheading(180)
            t.fd(20)
            t.setheading(270)
            t.fd(20)
            t.end_fill()

def moon(x, y):

    #main body
    t.setheading(180)
    t.color("black", "dark gray")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()
    t.color("black",  "gray")
    t.penup()
    t.goto(x+10, y-170)
    t.pendown()
    t.begin_fill()
    t.circle(10)
    t.end_fill()

    #detail #1
    t.penup()
    t.goto(x-30, y-10)
    t.pendown()
    t.begin_fill()
    t.circle(15)
    t.end_fill()

    #detail #2
    t.penup()
    t.goto(x+60, y-50)
    t.pendown()
    t.begin_fill()
    t.circle(17)
    t.end_fill()

    #detail #3
    t.penup()
    t.goto(x+20, y-100)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    #detail #4
    t.penup()
    t.goto(x-50, y-80)
    t.pendown()
    t.begin_fill()
    t.circle(13)
    t.end_fill()
    
def main():
    ground()
    building(-700, -160, 120, 320)
    building(-500, -160, 160, 600)
    building(-200, -160, 200, 400)
    building(100, -160, 240, 360)
    building(400, -160, 200, 520)
    moon(750, 470)
    base()
    driver_seat()
    windows()
    dirt()
    back_box()
    wheels(-300, -160)
    wheels(-180, -160)
    wheels(260, -160)
    wheel_frames()
    headlights(375, -70, 10)
    headlights(-400, -90, 7)
    box_details(-370, -30, 130)
    box_details(-270, -30, 136)
    box_details(-170, -30, 144)
    box_details(-70, -30, 151)
    box_details(30, -30, 158)



main()