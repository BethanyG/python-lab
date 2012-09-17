# Python Files

Last time, we ran all of our Python commands from the `>>>` prompt.
Interactive commands are good for experimentation, but we also want to save our work in files.

1. Run `IDLE` from the Start Menu.
1. Click on `File > New Window` in the menu.

You now have a window called "Untitled". It's empty, so let's type some code.

```python
import turtle

turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
turtle.forward(200)
turtle.right(90)
```

Writing our commands into a file let's us save our work,
and we can run all of these commands at once.

*Click on `Run > Run Module` or press `F5` to run this program.*

You will have to save your file before it will run.
Choose any name you want, like `mycode.py`.
Save it to your `Desktop`.

IDLE will then run the code, drawing a square, and will give you a new `>>>` prompt to run additional commands.

# Functions

A *function* is a collection of commands grouped together in a single command.

For example:

```python
import turtle

def square():
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
```

Now we have a new command, `square()`, that we can run any time.

Click `Run > Run Module` or press `F5`, then type `>>> square()` at the prompt.

# Your Turn

Write a function that draws something of your own,
then use your function to draw it over and over again quickly!

# Bonus

Visit https://github.com/michaelmp/python-lab/blob/master/labs/lab2.py and try some of functions.