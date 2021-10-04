# this is a test program from Qazi tutorial
import turtle

my_turtle = turtle.Turtle()
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)
my_turtle.right(90)
my_turtle.forward(100)
my_turtle.left(90)
my_turtle.forward(100)


def square(length, angle):
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)
    my_turtle.left(angle)
    my_turtle.forward(length)


for i in range(4):
    square(50, 90)

print(square)
