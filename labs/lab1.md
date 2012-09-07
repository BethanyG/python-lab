Python Laboratory
---

# Welcome to Python!

Python is a computer programming language.
Python helps you tell the computer what you want to do.
With Python, you can:

* Draw computer graphics.
* Make games.
* Build a website.
* Solve problems in math and science.
* ... and much much more!

In this lab, we're going to focus on making computer graphics.

# The Language

Learning Python is a lot like learning English, Spanish, or any spoken language.
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

The `>>>` is called a "prompt." The prompt is waiting for your Python command.
You can type in something like `1 + 1`, press the `Enter` key, and the computer will write back the answer.

If you ever want to remember something, computers have lots of memory.

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

You can draw a circle:
```python
turtle.circle(200)
```

# 

# Challenge

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