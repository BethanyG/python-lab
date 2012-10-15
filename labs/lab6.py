import turtle
screen = turtle.Screen()

def move():
    turtle.forward(100)

screen.onkey(move, "space")

def click(x, y):
    turtle.goto(x, y)

screen.onclick(click)

def turn():
    turtle.left(15)
    screen.ontimer(turn, 100)

screen.ontimer(turn, 100)

screen.listen()
screen.mainloop()