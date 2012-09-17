import turtle
from math import sin, pi

def square():
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)

def heart(size, shape):
    turtle.pensize(10)
    radius = size * sin(shape * pi / 180) / (1 + sin((90 - shape) * pi / 180))
    turtle.right(shape)
    turtle.forward(size)
    turtle.circle(radius, 180 + shape)
    turtle.right(180)
    turtle.circle(radius, 180 + shape)
    turtle.forward(size)
    turtle.left(180 - shape)

def at(x, y):
    turtle.penup()
    turtle.home()
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(y)
    turtle.pendown()

def wheel():
    turtle.pensize(10)
    turtle.pencolor("black")
    turtle.right(90)
    turtle.circle(50)
    turtle.left(90)

def chassis():
    heart(200, 60)

def car():
    at(150, 0)
    wheel()
    at(-150, 0)
    wheel()
    at(0, 25)
    chassis()

#### Now for something completely different ####

colors = ["red", "orange", "yellow", "green", "blue", "purple", "violet"]

def color(iteration):
    turtle.pencolor(colors[iteration % len(colors)])

def spirograph():
    turtle.delay(0)
    turtle.pensize(3)
    at(0, -200)
    for iteration in range(1, 100):
        color(iteration)
        turtle.circle(400, 80)
        turtle.circle(50, 175)

def hearts():
    turtle.delay(0)
    for iteration in range(1, 50):
        color(iteration)
        at(0, iteration * -5)
        heart(iteration * 10, 45)
        
#### And a bonus! ####

# What happens if we use a function within itself?
def spiral(size):
    turtle.pensize(1)
    turtle.delay(20)
    turtle.circle(size, 90)
    spiral(size * 1.1)
