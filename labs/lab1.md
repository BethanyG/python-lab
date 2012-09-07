# Welcome to Python!

Python is a *computer programming language*.
Python helps you tell the computer what you want to do.
With Python, you can:

* Draw pictures. http://www.blender.org/
* Make games. http://www.eveonline.com/
* Build a company. https://www.dropbox.com/
* Solve science problems. http://www.slac.stanford.edu/
* Take over the world. http://www.google.com/
* ... and much much more!

In this lab, we're going to focus on making computer graphics.

# Getting Started

Make sure you have Python installed on your computer.
From the Windows Start Menu, run `IDLE (Python GUI)`.

If IDLE isn't installed, visit http://python.org/download/ in your web browser, and install Python 3.2.3. 

# The Language

Learning Python is a lot like learning English, Español, Français or any other spoken language.
The only difference is you're speaking with a computer.
A computer language like Python translates human words into computer words.

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
>>> turtle.reset()
>>> turtle.home()
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(50)
>>> turtle.left(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.forward(50)
>>> turtle.left(180)
>>> turtle.forward(50)
>>> turtle.right(90)
>>> turtle.forward(100)
>>> turtle.left(90)
>>> turtle.circle(50, 180)
>>> turtle.forward(50)
>>> turtle.left(90)
>>> turtle.forward(20)
>>> turtle.left(90)
>>> turtle.forward(30)
>>> turtle.right(90)
>>> turtle.forward(20)
>>> turtle.right(90)
>>> turtle.forward(30)
>>> turtle.right(90)
>>> turtle.forward(40)
>>> turtle.right(180)
```
(You can tell I'm a gifted artist!)

Now draw something of your own.

**Raise your hand and show me your drawing when you're done.**

*Hint* If you want to move the turtle without drawing anything, `turtle.penup()` will
stop drawing when the turtle moves, and `turtle.pendown()` will continue drawing.
This will be handy if I want to draw windows on my house.

# Advanced Topic: Functions

Let's look at something really tricky.

* Download `lab1.py` from the `labs` folder. https://raw.github.com/michaelmp/python-lab/master/labs/lab1.py
* In IDLE, go to `File > Open` and open `lab1.py`. A new window will appear.

The file `lab1.py` is an example of a *source* file.
It has all of the instructions you could give to the *prompt* (remember: `>>>`),
but you only have to type it once.
A prompt is handy when you want to experiment with commands interactively.
A source file is handy when you want to save your commands for later, or run them all at once.

* In the `lab1.py` window, go to the menu `Run > Run Module`.

Now you can give new commands to the prompt:
```python
>>> small_circle()
>>> big_circle()
>>> circle(300)
```

These commands did not exist until you ran `Run > Run Module`.
In `lab1.py`, I *defined* `small_circle` as:
```python
def small_circle():
    turtle.circle(100)
```

`small_circle` is a *function*. A function does everything after the `:` symbol everytime you mention its name.

So every time you give the command `>>> small_circle()` at the prompt,
the computer will also run `turtle.circle(100)` for you.

Functions are handy when you have a lot of commands to repeat over and over again.
(You'll hurt your hands if you type too much!)
So let's look back at that picture we drew.
I was making a house.

Let's *define* a new *function* that draws that house.
It will have all of the same commands I wrote before, following the `def house():` line of code.
```python
def house():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(180)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.circle(50, 180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(20)
    turtle.left(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(20)
    turtle.right(90)
    turtle.forward(30)
    turtle.right(90)
    turtle.forward(40)
    turtle.right(180)
```

*Now*, whenever I want to draw a house, I can just type `house()`.

# Challenge

Okay, it's your turn. Please write a function that draws a square:
```python
def square():
    # YOUR CODE GOES HERE
```

Then you can draw a lot of squares!

```python
>>> square()
>>> turtle.forward(100)
>>> square()
>>> turtle.left(45)
>>> square()
```

**Please raise your hand and show me your squares when you're done.**

# Challenge

In `lab1.py`, *define* the function `picture()` with anything you want to draw.

*Hint*: Now you can use `square()` inside of `picture()` to draw squares quickly.

*Hint*: You can also use the `circle()` function inside of `picture()`.

*Hint*: What happens if you use `picture()` inside of `picture()`?

When you're done, `Run > Run Module` and `>>> picture()` to see what happens.

# Saving your work.

Go to the menu, `File > Save` to save your *source* file.

**Remember to save your changes to `lab1.py` so you can continue later.**