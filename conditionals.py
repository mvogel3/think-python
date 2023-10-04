import time
import math
import turtle

x = 2
y = 5
# chained conditonals example
if x < y:
    print('x is less than y')
elif x > y:
    print('x is greater than y')
else:
    print('x and y are equal')

# changing x value but not y value
x = 7
# nested conditional examples
if x == y:
    print('x and y are equal')
else:
    if x < y:
        print('x is less than y')
    else: 
        print('x is greater than y')

if 0 < x:
    if x < 10:
        print('x is a positive single-digit number')
# print statement only runs if we make it past both conditionals
if 0 < x and x < 10:
    print('x is a positive single-digit number')

# more concise option with Python 3
if 0 < x < 10:
    print('x is a positive single-digit number')

# 5.8 Recursion
def countdown(n):
    """function passes n-1 until n equals 0"""
    if n <= 0:
        print('Blastoff!')
    else: 
        print(n)
        countdown(n-1)
# countdown(5)

def count_down2(n):
    if n <=0:
        return
    print(n)
    count_down2(n-1)

count_down2(10)

# recursive function that works similar to a for loop
def print_n(s, n):
    if n<= 0:
        return
    print(s)
    print_n(s, n-1)

# print_n('hi', 10)

# accidental infinitely recursive function
def count_down(n):
    print(n)
    count_down(n-1)

# count_down(10)

# name = input('What is your name?\n')

# 5.14 Exercises

t = time.time()

def current_time(t):
    n = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(time.time()))
    days = t // 86400
    print(f'it has been {days} days since the epoch')
    print(f'the current time is {n}')

current_time(t)

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Fermat's Last Theorem was wrong!")
    elif n == 2 and a**n + b**n == c**n:
        print(f'{a**n} + {b**n} = {c**n}')
    else:
        print("No, that doesn't work. Try again.")
check_fermat(4, 5, 6, 2)

def input_fermat():
    a = input("Please choose an a value: ")
    b = input("Please choose a b value: ")
    c = input("Please choose a c value: ")
    n = input("Please choose an n value: ")
    a = int(a)
    b = int(b)
    c = int(c)
    n = int(n)
    return check_fermat(a, b, c, n)

# input_fermat()

def is_triangle(q, r, s):
    if q+r>s and q+s>r and r+s>q:
        print("YES")
    else:
        print("NO")
# is_triangle(12, 4, 5)

def input_triangle():
    q = int(input('q: '))
    r = int(input('r: '))
    s = int(input('s: '))
    return is_triangle(q, r, s)
# input_triangle()

def recurse(n, s):
    """as n becomes smaller, s becomes larger. when n finally equals 0, 
    the ourput is 0 plus the previous sum of n+s"""
    if n == 0:
        print(s)
    else:
        recurse(n-1, n+s)
# recurse(3, 0)
# recurse(-1, 0) results in Recursion Error: maximum recursion exceeded in comparison

bob = turtle.Turtle()
def draw(p, length, n):
    if n == 0:
        return
    angle = 50
    p.fd(length*n)
    p.lt(angle)
    draw(t, length, n-1)
    p.rt(2*angle)
    draw(t, length, n-1)
    p.lt(angle)
    p.bk(length*n)
# draw(bob, 10, 3)

turtle.done()


