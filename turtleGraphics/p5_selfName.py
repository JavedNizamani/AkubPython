from turtle import *

# align left
speed(1)
pensize(10)
shape("turtle")
turtlesize(3)
penup()
goto(-200, 150)
# letter J
pendown()
color("red")
right(90)
fd(150)
circle(-60, 180)

penup()
right(90)
fd(170)
left(90)
forward(150)

# letter A
pendown()
color("blue")
right(190)
fd(200)
bk(200)
left(30)
fd(200)
bk(80)
right(110)
fd(60)

penup()
right(90)
fd(120)
right(90)
fd(50)

# letter V
pendown()
color("green")
right(70)
forward(220)
left(150)
fd(220)

penup()
right(80)
fd(30)

# letter E
pendown()
color("pink")
right(90)
fd(200)
left(90)
fd(100)
bk(100)
left(90)
fd(100)
right(90)
fd(100)
bk(100)
left(90)
fd(100)
right(90)
fd(100)

penup()
fd(20)
# letter D
pendown()
color("red")
right(90)
fd(200)

left(90)
circle(100, 180)

# finally hide the turtle

hideturtle()

exitonclick()