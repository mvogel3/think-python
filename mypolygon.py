# cloned PythonData env
# brew installed python-tk
# needed to run on a Python shell???

import turtle


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
def polygon(t, length, n):
    angle = 360/n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

polygon(bob, 90, 8)

def circle(t, r):
    polygon(bob, 10, 360)

circle(bob, 5)


turtle.done()