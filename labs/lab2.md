# Practical Python

In this lab we're going to learn some general Python,
then we'll apply it to Turtle Graphics to draw complex pictures.

* Start up IDLE the same way you did in Lab 1.

# Data Types

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

A *string* is another name for text.
A string begins and ends with a quote symbol, `"` or `'`.
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

# Lists

In your IDLE prompt:
```python
>>> [1, 2, 3]
[1, 2, 3]
```

You can create a list of things in Python with *square brackets*, `[` and `]`.

