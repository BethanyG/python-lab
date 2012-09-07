# Practical Python

In this lab we're going to learn some general Python,
then we'll apply it to Turtle Graphics to draw complex pictures.

* Start up IDLE the same way you did in Lab 1.
* Remember to `import turtle` before you draw pictures.

# Data Types

"Data" means information.

The two basic data types we will be working with are *numbers* like `1`, `2`, `3`,
and *strings*, like `"How are you today?"`.

A *number* can be expressed in several ways:
```python
>>> 100
100
>>> 100.0
100.0
>>> 100/1
100.0
>>> 1e2
100.0
```

"String" is just another name for written words.
A *string* begins and ends with a quote symbol, `"` or `'`.
```python
>>> "It was the best of times, it was the worst of times..."
'It was the best of times, it was the worst of times...'
```

# Variables

When you want to remember something, a *variable* can remember it for you.

So I can remember the number `10`, with a *variable* called `ten`.
```python
>>> ten = 10
```

And I can retrieve the number by referring to the variable `ten`.
```python
>>> ten
10
>>> ten + ten
20
>>> ten * ten
100
```

**Challenge:** Create a variable called `name` that remembers your name as a *string*.
Then run `>>> print(name)`

# Turtle Graphics

Okay. Now that we know how to remember numbers with variables, let's put it to use.

In Lab 1, we learned about *functions*. Remember?
```python
def square():
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
```

`square` is a function. You can run `square()` to run all of the code inside of the function.

Notice that `square` draws a square with sides that are `100` long.
What if we wanted a square with sides `50` long?

* We could write a whole new function, just for squares 50 long.
* Or, we could use a *variable*!

```python
length = 100

def square():
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
    turtle.forward(length)
    turtle.left(90)
```

`length` is the variable. Every time the computer runs `turtle.forward(length)`,
it asks `length` for the stored value, which is `100`.

But now, we could do this:

```python
>>> length = 50
>>> square()
```

Or this:

```python
>>> length = 200
>>> square()
```

And we get the square we want.

---

We can do the same thing for colors!

The value of a color is stored as *string* data.

For example, `"red"` and `"#ff0000"` are both the color red.

*Hint*: `"#ff0000"` is a strange way to name a color.
A color palette can help you come up with these names.
http://www.color-hex.com/color-wheel/

In Turtle Graphics, you can change color with *pencolor*:
```python
>>> color = "red"
>>> turtle.pencolor(color)
```

Here, `color` is a variable, and it is remembering the data `"red"`.

# Lists

In your IDLE prompt, please type:
```python
>>> [1, 2, 3]
[1, 2, 3]
```

`[1, 2, 3]` is a *list* of data, the numbers `1`, `2`, and `3`, in that order.

You can create a list of things in Python with *square brackets*, `[` and `]`.
You must separate your data by commas, `,`.

Let's store some colors in a variable!
```python
>>> colors = ["red", "blue", "green", "purple"]
```

Whenever we want to find that list, just type `colors`.
```python
>>> colors
['red', 'blue', 'green', 'purple']
```

# Iteration

Things are about to get exciting now!

One thing we can do with lists is *iterate*.
Iteration is where you repeat some commands for every thing in a list.

For example:
```python
>>> for color in colors:
        turtle.pencolor(color)
        turtle.forward(50)
        
```

What happened?

**Raise your hand and explain to a teacher what just happened.**

---

There is a Turtle Graphics command called `pensize`.
```python
>>> turtle.pensize(10)
>>> turtle.forward(100)
```

Here's an *iteration* that changes pen size:
```python
>>> for size in [10, 20, 30, 40, 50]:
        turtle.pensize(size)
        turtle.forward(size)

```

# Challenge

When you're ready, download `lab2.py`.

`lab2.py` contains an incomplete function called `spirograph`.
Your job is to complete the function.

First, let's read up on what a Spirograph is: 
http://en.wikipedia.org/wiki/Spirograph

Remember to go to `Run > Run Module`, then you can run the function `>>> spirograph()`.

*Hint*: If you want to speed up the drawing, run `turtle.delay(0)`.

---

## Step 1

Come up with a new pattern of your own.

You might get some ideas here: http://en.wikipedia.org/wiki/File:Various_Spirograph_Designs.jpg

*Hint*: The `turtle.circle` function can be used to create semi-circles and arcs.
In `turtle.circle(50, 180)`, the `50` is the radius of the circle,
and the `180` is how many degrees in the circle are drawn.

## Step 2

Let's add some color.

You'll find a function called `color` in `lab2.py`.
`color(0)` will set the pen color to the first color listed in `colors`.
`color(1)` will set the pen color to the second color listed in `colors`.
`color(2)` will set the pen color to the third color, and so on...

If there aren't enough colors in `colors`, then it starts over from the beginning of the list.

So you could get a new color listed in `colors` with each iteration:
```python
def spirograph():
    for iteration in range(1, 1000):
        color(iteration)
        # ... the rest of your code ...
```

`lab2.py` comes with only one color:
```python
colors = ["black"]
```

But you can add as many colors as you want!
Visit http://www.color-hex.com/color-wheel/ and find some fun colors to add to the list.

For example, `"#b01db5"` is a violet, `"#0faed6"` is sky blue, and `"#baa057"` is a bister.

## Step 3

When you're all done, **show the class your picture!**

## Step 4

Remember to save `lab2.py` with your spirograph drawing!

# Bonus: Publish your work!

After you have finished your spirograph, it's time to learn a little bit about the Internet.
Let's save the picture you made and put it on the Internet where everyone else can find it.

## Step 1: Save your picture.

Press the `Print Screen` key on your keyboard. It's hidden at the far right.

Now, open `Paint` from the Windows Start Menu.

Click on the menu, `Edit > Paste`.
Now you have a big picture of what was on the screen when you pressed `Print Screen`.

"Crop" the picture down to just your spirograph picture, then go to the menu, `File > Save As`.

Save your picture as a `PNG` file.

## Step 2: Email

Getting an email account is easy and free.

An email account lets you send messages to friends and family.

It is also a way for Internet companies to communicate with you.

...

## Step 3: Online Storage

Until now, the lab files you have been saving have been stored on the
school's computers.

You can also store files on the Internet.

One advantage is that you can give your friends and family a *hyperlink* to your file,
and they can access it from any web browser on any computer, anywhere in the world.

https://github.com/michaelmp/python-lab/blob/master/labs/lab2.md is a hyperlink to this file,
the one you are reading _right now_!

---

Now that you have an email address, you can sign up for Internet services.
Many are free.

Over **2.2 billion** people are on the Internet! Why not you?

Let's sign up for one service at: https://www.dropbox.com/register

You will need to enter your Name (or an *alias* if you want to remain anonymous),
an Email Address (you just signed up for one!),
and a password.

DropBox is an example of a *file hosting service*.
They'll hold onto your files if you don't have any other place to put them.

Because they are eager for your business, DropBox will give you **2 gigabytes** of free storage.

**Challenge**: How big is a *gigabyte*?

*Hint*: *giga* means a billion, and every letter of Python you type is one *byte*.

## Step 4: Photo Gallery

Now that you've got an *email address* and a *file host*, you're ready to publish your picture!

...