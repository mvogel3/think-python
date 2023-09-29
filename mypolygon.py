# renamed turtle.py. can't have module name in the file name
# cloned PythonData env
# brew installed python-tk
# needed to run on a Python shell???

import turtle
import math

bob = turtle.Turtle()

print(bob)
# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

square(bob, 200)
def polygon1(t, n, length):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon1(bob, 8, 90)

def circle1(t, r):
    # first attempt at a circle. just makes a giant octagon
    polygon1(bob, 10, 360)

circle1(bob, 5)

def circle2(t, r):
    circumference = 2 * math.pi * r
    n = 70
    length = circumference / n
    polygon1(t, n, length)

circle2(bob, 95)

def arc1(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n

    for i in range(n):
        t.fd(step_length)
        t.lt(step_angle)

def polyline(t, n, length, angle):
    """draws n line segments with the given length and angle 
    (in degrees) between them. 
    t is a turtle. """
    for i in range(n):
        t.fd(length)
        t.lt(angle)


def polygon(t, n, length):
    angle = 360/n
    polyline(t, n , length, angle)

def arc(t, r, angle):
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)

def circle(t, r):
    arc(t, r, 360)

circle(bob, 95)
turtle.done()