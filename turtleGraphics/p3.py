from turtle import Turtle
from random import random

t = Turtle()
t1 = Turtle()
for i in range(100):
    steps = int(random() * 100)
    angle = int(random() * 360)
    t.right(angle)
    t.fd(steps)

    t1.left(30)
    t1.fd(steps)

t.screen.mainloop()