# Practical Python

In this lab we're going to learn some general Python,
then we'll apply it to Turtle Graphics to draw complex pictures.

* Start up IDLE the same way you did in Lab 1.

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

Let's do the same thing for colors!

The value of a color is stored as *string* data.

For example, `"red"` and `"#ff0000"` are both the color red.

# Lists

In your IDLE prompt:
```python
>>> [1, 2, 3]
[1, 2, 3]
```

You can create a list of things in Python with *square brackets*, `[` and `]`.

