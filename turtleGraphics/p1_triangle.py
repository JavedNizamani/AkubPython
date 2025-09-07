from turtle import *

speed(1)
bgcolor("light blue")

penup()
goto(-150, -100)
fillcolor("yellow")
begin_fill()

pendown()
# fd(300)
# left(120)
# fd(300)
# left(120)
# fd(300)

for i in range(3):
    fd(300)
    left(120)

end_fill()
hideturtle()

exitonclick()