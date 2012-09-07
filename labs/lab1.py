import turtle

# Draw a small circle.
def small_circle():
    turtle.circle(100)

# Draw a big circle.
def big_circle():
    turtle.circle(500)

# Draw any size circle.
def circle(radius):
    turtle.circle(radius)

# Try running:
#
# >>> small_circle()
#
# >>> big_circle()
#
# >>> circle(300)

def house():
    turtle.reset()
    turtle.home()
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.goto(0, 100)
    turtle.goto(100, 100)
    turtle.left(90)
    turtle.circle(50, 180)