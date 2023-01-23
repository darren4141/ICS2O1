'''
=====================================================================================================================================================================
Turtle graphics self portrait
DARREN LIU
1/25/2022
PYTHON VER 3.7.0
=====================================================================================================================================================================
PROBLEM DEFINITION: Draw a self portrait using turtle graphics
INPUT(N/A)
OUTPUT: Self Portrait and background
=====================================================================================================================================================================
'''


from turtle import *
t=Turtle()
s=Screen()
s.setup(1000, 1000)
t.screen.bgcolor("sky blue")
t.hideturtle()
t.speed(0)

def face(x, y):
    #face
    t.color("wheat")
    t.penup()
    t.goto(x, y)
    t.pendown
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def eyes(x, y):
    #eyes
    t.color("black", "white")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.left(135)
    t.circle(15, 90)
    t.left(90)
    t.circle(15, 90)
    t.end_fill()

def ears(x, y):
    #ears
    t.color("black", "tan")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(7)
    t.end_fill()

def pupils(x, y):
    #pupils
    t.color("black")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(3)
    t.end_fill()

def mouth(x, y):
    #mouth
    t.color("pink")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    #shape the mouth
    t.color("wheat")
    t.penup()
    t.goto(x, y+5)
    t.pendown()
    t.begin_fill()
    t.circle(25)
    t.end_fill()

def nose(x, y):
    #nose
    t.color("black", "tan")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(5, 180)
    t.end_fill()

def hair(x, y):
    t.color("black", "black")

    #right side
    t.penup()
    t.goto(x-13, y)
    t.pendown()
    t.begin_fill()
    t.left(100)
    t.circle(60, 90)
    t.left(90)
    t.circle(60, 90)
    t.end_fill()

    
    #left side
    t.penup()
    t.goto(x-8, y+2)
    t.pendown()
    t.begin_fill()
    t.right(10)
    t.circle(40, 90)
    t.left(90)
    t.circle(40, 90)
    t.end_fill()

def glasses(x, y):
    
    t.color("black")
    t.penup()

    #left lens
    t.goto(x, y)
    t.pendown()
    t.circle(20, 180)
    t.goto(x+45, y)
    t.left(180)

    #right lens
    t.circle(20, 180)
    t.pensize(2)
    t.goto(x, y)
    t.pensize(1)

def shirt():
    t.color("black", "white")

    #shirt
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.begin_fill()
    t.left(90)
    t.fd(50)
    t.left(90)
    t.fd(200)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(200)
    t.left(90)
    t.fd(50)
    t.end_fill()

    #shirt strings
    t.left(90)
    t.pensize(3)

    #left string
    t.penup()
    t.goto(-10, 0)
    t.pendown()
    t.color("black")
    t.fd(30)
    t.color("DarkGrey")
    t.fd(10)

    #right string
    t.penup()
    t.left(180)
    t.fd(40)
    t.right(90)
    t.fd(20)
    t.right(90)
    t.pendown()
    t.color("black")
    t.fd(30)
    t.color("DarkGrey")
    t.fd(10)

    #shirt text
    t.penup()
    t.goto(-35, -60)
    t.pendown()
    t.color("black")
    t.write("ANTI \n SOCIAL \n SOCIAL \n CLUB", font=("Times New Roman", 6))


    t.pensize(1)

def arms():
    t.color("white")

    #right arm
    t.penup()
    t.goto(50, -15)
    t.setheading(45)
    t.pendown()
    t.begin_fill()
    t.fd(125)
    t.setheading(315)
    t.fd(30)
    t.setheading(225)
    t.fd(160)
    t.end_fill()

    #left arm
    t.goto(-50, -15)
    t.setheading(135)
    t.pendown()
    t.begin_fill()
    t.fd(125)
    t.setheading(225)
    t.fd(30)
    t.setheading(315)
    t.fd(160)
    t.end_fill()

    #right hand
    t.color("wheat")
    t.penup()
    t.goto(145, 55)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()

    #left hand
    t.color("wheat")
    t.penup()
    t.goto(-170, 55)
    t.pendown()
    t.begin_fill()
    t.circle(20)
    t.end_fill()


def pants():
    #pants
    t.color("DarkBlue")
    t.penup()
    t.goto(50, -200)
    t.pendown()
    t.begin_fill()
    t.setheading(270)
    t.fd(200)
    t.setheading(180)
    t.fd(40)
    t.setheading(93)
    t.fd(200)
    t.setheading(267)
    t.fd(200)
    t.setheading(180)
    t.fd(40)
    t.setheading(90)
    t.fd(200)
    t.end_fill()

    #stripes
    t.color("white")
    t.pensize(3)
    t.penup()
    t.goto(46, -200)
    t.pendown()
    t.setheading(270)
    t.fd(200)

    t.penup()
    t.goto(40, -200)
    t.pendown()
    t.setheading(270)
    t.fd(200)

    t.penup()
    t.goto(-46, -200)
    t.pendown()
    t.setheading(270)
    t.fd(200)

    t.penup()
    t.goto(-40, -200)
    t.pendown()
    t.setheading(270)
    t.fd(200)

    t.pensize(1)

    #pants text
    t.color("white")
    t.penup()
    t.goto(14, -210)
    t.write("adidas", font=("calibri", 6))


def shoes():
    #right shoe
    t.color("DarkGoldenrod3")
    t.penup()
    t.goto(70, -420)
    t.pendown()
    t.begin_fill()
    t.setheading(90)
    t.circle(20, 90)
    t.setheading(180)
    t.fd(40)
    t.setheading(270)
    t.fd(20)
    t.setheading(0)
    t.fd(60)
    t.end_fill()

    #right sole  
    t.penup()
    t.color("brown4")
    t.goto(70, -420)
    t.pendown()
    t.begin_fill()
    t.setheading(270)
    t.fd(5)
    t.setheading(180)
    t.fd(60)
    t.setheading(90)
    t.fd(5)
    t.setheading(0)
    t.fd(60)
    t.end_fill()
    

    #left shoe
    t.color("DarkGoldenrod3")
    t.penup()
    t.goto(-50, -400)
    t.pendown()
    t.begin_fill()
    t.setheading(180)
    t.circle(20, 90)    
    t.setheading(0)
    t.fd(60)
    t.setheading(90)
    t.fd(20)
    t.setheading(180)
    t.fd(40)
    t.end_fill()

    #left sole
    t.penup()
    t.color("brown4")
    t.goto(-10, -420)
    t.pendown()
    t.begin_fill()
    t.setheading(270)
    t.fd(5)
    t.setheading(180)
    t.fd(60)
    t.setheading(90)
    t.fd(5)
    t.setheading(0)
    t.fd(60)
    t.end_fill()

def grass():
    #grass
    t.color("green")
    t.penup()
    t.goto(1000, -425)
    t.pendown()
    t.setheading(180)
    t.begin_fill()
    t.fd(2000)
    t.setheading(270)
    t.fd(100)
    t.setheading(0)
    t.fd(2000)
    t.end_fill()
    

def circle_tree(x, y):

    #trunk
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.setheading(90)
    t.fd(600)
    t.setheading(180)
    t.fd(30)
    t.setheading(270)
    t.fd(600)
    t.setheading(0)
    t.fd(30)
    t.end_fill()

    #circle leaves
    t.color("green")
    t.penup()
    t.goto(x-15, y+550)
    t.pendown()
    t.begin_fill()
    t.circle(100)
    t.end_fill()

def triangle_tree(x, y):

    #trunk
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color("brown")
    t.begin_fill()
    t.setheading(90)
    t.fd(600)
    t.setheading(180)
    t.fd(30)
    t.setheading(270)
    t.fd(600)
    t.setheading(0)
    t.fd(30)
    t.end_fill()

    #triangular leaves
    
    t.color("green")
    for i in range (0, 6):
        t.penup()
        t.goto(x-200+(i*25), y+100+(i*100))
        t.pendown()
        t.begin_fill()
        for j in range(3):
            t.fd(400-(i*50))
            t.left(120)
        t.end_fill()

def bird(x, y):
    #left wing
    t.setheading(0)
    t.color("white")
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #right wing
    t.penup()
    t.goto(x+50, y)
    t.pendown
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #left cover
    t.color("sky blue")
    t.penup()
    t.goto(x, y-20)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #right cover
    t.penup()
    t.goto(x+50, y-20)
    t.pendown()
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #bird feet
    t.pensize(3)
    t.color("gold")
    t.penup()
    t.goto(x+10, y+78)
    t.pendown()
    t.setheading(225)
    t.fd(30)
    t.penup()
    t.goto(x+40, y+78)
    t.pendown()
    t.setheading(315)
    t.fd(30)
    
    t.pensize(1)


def sun():
    #sun
    t.color("gold")
    t.penup()
    t.goto(850,350)
    t.pendown
    t.begin_fill()
    t.circle(70)
    t.end_fill()

def bush(x, y):

    #back bush
    t.color("dark green")
    t.penup()
    t.goto(x+50,y+20)
    t.pendown
    t.begin_fill()
    t.circle(80)
    t.end_fill()

    #small back bush 
    t.color("sea green")
    t.penup()
    t.goto(x-60,y+30)
    t.pendown
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    
    
    #front bush
    t.color("lime green")
    t.penup()
    t.goto(x,y)
    t.pendown
    t.begin_fill()
    t.circle(80)
    t.end_fill()

    #small front bush 1
    t.color("green yellow")
    t.penup()
    t.goto(x-50,y-30)
    t.pendown
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    #small front bush 2
    t.color("yellow green")
    t.penup()
    t.goto(x+70,y-20)
    t.pendown
    t.begin_fill()
    t.circle(50)
    t.end_fill()

def main():
    
    grass()
    bird(-570, 400)
    bird(-400, 400)
    triangle_tree(-900, -430)
    circle_tree(-500, -430)
    triangle_tree(-100, -430)
    circle_tree(300, -430)
    triangle_tree(700, -430)
    sun()
    bush(-800, -490)
    bush(800, -460)
    bush(440, -440)
    bush(-400, -510)
    t.setheading(0)
    ears(50, 40)
    ears(-50, 40)
    face(0, 0)
    mouth(0, 10)
    eyes(-12, 57)
    t.right(45)
    eyes(28, 57)
    pupils(-20, 55)
    pupils(20, 55)
    t.right(135)
    glasses(-43, 62)
    t.left(135)
    t.right(225)
    nose(0, 27)
    hair(0, 110)
    shirt()
    arms()
    pants()
    shoes()

main()