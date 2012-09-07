Python Laboratory
---

# Welcome to Python!

Python is a computer programming language.
Python helps you tell the computer what you want it to do.
With Python, you can:

* Draw computer graphics
* Make games
* Build a website
* Solve problems in math and science
* ... and more!

In this lab, we're going to focus on making computer graphics.

# Getting Started

Make sure you have Python installed on your computer.
From the Windows Start Menu, run `IDLE (Python GUI)`.

If IDLE isn't installed, visit http://python.org/download/ in your web browser, and install Python 3.2.3. 

# Turtle Graphics

First, you need to load Turtle Graphics:
    
```python
import turtle
```
    
Then, you can draw pictures:
    
```python
turtle.forward(100)
turtle.left(90)
turtle.forward(200)
```

You can change the color:
    
```python
turtle.pencolor("red")
```

You can change the background color:
    
```python
turtle.bgcolor("blue")
```



# 

# Challenge

Write a function that draws a square.

```python
def square():
    # YOUR CODE GOES HERE
```

Draw a lot of squares!

```python
turtle.goto(100, 100)
square()

turtle.goto(-100, 0)
square()

turtle.goto(200, 0)
square()
```