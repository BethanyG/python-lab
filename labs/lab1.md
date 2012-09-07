Python Laboratory
---

# Welcome to Python!

Python is a *computer programming language*.
Python helps you tell the computer what you want to do.
With Python, you can:

* Draw computer graphics.
* Make games.
* Build a website.
* Solve problems in math and science.
* ... and much much more!

In this lab, we're going to focus on making computer graphics.

# Getting Started

Make sure you have Python installed on your computer.
From the Windows Start Menu, run `IDLE (Python GUI)`.

If IDLE isn't installed, visit http://python.org/download/ in your web browser, and install Python 3.2.3. 

# The Language

Learning Python is a lot like learning English, Español, Français or any other spoken language.
The only difference is you're talking with a computer.
A computer language like Python translates human work into computer work.

After loading IDLE, you will see something like this:

```
Python 3.2.3 (default, Apr 11 2012, 07:15:24) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
```

Just to get warmed up, let's do a little math:
```python
>>> 1 + 1
2
```

The `>>>` is called a *prompt*. The prompt is waiting for your Python command.
You can type in something like `1 + 1`, press the `Enter` key, and the computer will write back the answer.

If you ever want to remember something, computers can help you remember.

```python
>>> five = 2 + 3
```

Now, if you ever want to know what `2 + 3` is, you can just say `five`.

```python
>>> five
5
```

You can do multiplication with the `*` key (press `Shift`+`8`).

```python
>>> five * five
25
```

That's all for now. We'll learn more about the language later.

# Turtle Graphics

First, you need to load Turtle Graphics:
    
```python
>>> import turtle
```
    
Then, you can draw pictures:
    
```python
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(200)
```

You can change the color:
    
```python
>>> turtle.pencolor("red")
```

You can change the background color:
    
```python
>>> turtle.bgcolor("blue")
```

You can draw a circle:
```python
>>> turtle.circle(200)
```

Whenever you want to erase everything and start fresh:
```python
>>> turtle.reset()
```

# Challenge

Draw a picture of something using lines and circles.
For example, here's a house I made:

```python
>>> turtle.home()
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.goto(0, 100)
>>> turtle.goto(100, 100)
>>> turtle.left(90)
>>> turtle.circle(50, 180)
```
(You can tell I'm a gifted artist!)

Now draw something of your own.

**Raise your hand and show me your drawing when you're done.**

*Hint* If you want to move the cursor without drawing anything, `turtle.penup()` will
stop drawing when the turtle moves, and `turtle.pendown()` will continue drawing.
This will be handy if I want to draw windows on my house.

# Functions

Let's look at some harder things.

* Download `lab1.py` from `labs` folder.
* In IDLE, go to `File > Open` and open `lab1.py`. A new window will appear.
* In this window, go to `Run > Run Module`.

Now you can give new commands like:
```python
>>> small_circle()
```

In `lab1.py`, I *defined* `small_circle` as:
```python
def small_circle():
    turtle.circle(100)
```

`small_circle` is a *function*. A function does everything after the `:` symbol everytime you mention its name.

So every time you give the command `small_circle()`, the computer will also run `turtle.circle(100)` for you.

Functions are handy when you have a lot of commands to give over and over again.
You'll hurt your hands if you type too much!
So let's look back at that picture we drew.
I was making a house.

Let's *define* a new *function* that draws that house.
It will have all of the same commands I wrote before, following the `def house():` line of code.
```python
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
```

Write a function that draws a square.

```python
def square():
    # YOUR CODE GOES HERE
```

Then you can draw a lot of squares!

```python
turtle.goto(100, 100)
square()

turtle.goto(-100, 0)
square()

turtle.goto(200, 0)
square()
```

**Please raise your hand and show me your squares when you're done.**