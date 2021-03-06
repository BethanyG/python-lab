# Turtle Graphics: Cheat Sheet

Get started:
```python
import turtle
```

Draw a line, 100 pixels long:
```python
turtle.forward(100)
```
```python
turtle.back(100)
```

Change direction, right or left by 90 degrees:
```python
turtle.right(90)
```
```python
turtle.left(90)
```

Draw a circle, with radius 50 pixels:
```python
turtle.circle(50)
```

Draw a semi-circle:
```python
turtle.circle(50, 180)
```

Change the color:
```python
turtle.pencolor("blue")
```

Change the pen size to 10 pixels:
```python
turtle.pensize(10)
```

Erase everything and start over:
```python
turtle.reset()
```

Send the turtle to center of the screen:
```python
turtle.home()
```

Move the turtle without drawing:
```python
turtle.penup()
```

Resume drawing when turtle moves:
```python
turtle.pendown()
```

Make the turtle draw faster:
```python
turtle.delay(0)
```