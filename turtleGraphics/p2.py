import turtle

my_turtle = turtle.Turtle(shape = "turtle")
my_turtle1 = turtle.Turtle(shape = "turtle")


my_turtle.speed(1)
my_turtle1.speed(1)
my_turtle.up()
my_turtle1.up()

my_turtle.width(10)
my_turtle1.width(5)
for steps in range(40):
    for c in ('blue', 'red', 'green'):
        my_turtle.color(c)
        my_turtle1.color(c)
        my_turtle.forward(steps)
        my_turtle1.fd(steps)
        my_turtle.left(10)
        my_turtle1.right(15)

# for step2 in range(20):
#     for d in ('yellow', 'cyan', 'black'):
#         my_turtle1.color(d)
#         my_turtle1.fd(step2)
#         my_turtle1.right(10)

my_turtle.done()