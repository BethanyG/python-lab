import turtle

colors = ["black"]

def color(iteration):
    turtle.pencolor(colors[iteration % len(colors)])

def spirograph():
    for iteration in range(1, 1000):    
        # Example (REPLACE WITH YOUR OWN DESIGN):
        turtle.forward(300)
        turtle.right(170)