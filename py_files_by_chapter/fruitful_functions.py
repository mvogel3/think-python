import math

# in the function below, "a" is a temporary variable
def area(radius):
    a = math.pi * radius**2
    return a
# print(area(4))

def compare(x, y):
    if x > y:
        return 1
    if x == y:
        return 0
    if x < y:
        return -1
    
# print(compare(3, 7))

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    
# print(absolute_value(-6))

def distance(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result # final increment. all previous testing is now dead code. 
# scaffolding left in for learning purposes.
    print(f'dsquared is {dsquared}') # increment 3
    print(f'dx is {dx}') # increment 2
    print(f'dy is {dy}') # increment 2 
    return 0.0 # increment 1


print(distance(1, 2, 4, 6)) #print statement would also not be in final function invocation

def hypotenuse(a, b):
    a2 = a**2
    b2 = b**2
    c = math.sqrt(a2 + b2)
    return c
    return round(c, 2)
    print(f'a-squared plus b-squared equals {a2 + b2}')
    return a + b
print(round(hypotenuse(4, 7), 2)) 
# using the round function to round down to the nearest 2 decimals. can't decide whether 
# to use it in the function or outside of it. may depend on the use case

# function that calls both area and distance functions using a compound expression
def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def is_divisible(x, y):
    return x % y == 0 # no need to add the conditional. result of == is a boolean
    if x % y == 0:
        return True
    else:
        return False
# is_divisible(250, 7)
if is_divisible(250, 5):
    print('x is divisible by y')

def is_between(x, y, z):
    return x <= y <= z # if the arguments aren't satisfactory, the function returns False
if is_between(5, 25, 15):
    print('y is between x and z')
else:
    print('y is not between x and z')      

def factorial(n):
    if n == 0:
        return 1
    else: # using the else because first condition is a boolean??
        recurse = factorial(n-1)
        result = n * recurse
        return result

def fibonacci(n):
    """another recursive function used to return the next fibonacci number?"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        # print(fibonacci(n-1))
        # print(fibonacci(n-2))
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(7))
def factorial_revised(n):
    if not isinstance(n, int):
        print('Factorial is only designed for integers.')
        return None
    elif n < 0:
        print('Factorial is not defined for negative integers')
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial_revised(n-1)
    

def b(z):
    prod = a(z, z) # prod = a passing z as both x and y 
    print(z, prod)
    return prod
def a(x, y):
    x = x + 1
    return x * y
def c(x, y, z):
    total = x + y + z
    square = b(total)**2
    return square
x = 1
y = x + 1
print(c(x, y+3, x+y))

def ack(m, n):
    """ackermann function"""
    if m == 0:
        return n + 1
    if m > 0 and n ==0:
        return ack(m-1, 1)
    if m > 0 and n > 0:
        return ack(m-1, ack(m, n-1))
# print(ack(3, 4))


def is_palendrome(word):
    """slices the string and reverses it"""
    if word == word[::-1]:
        return True
    else: 
        return False
def isPalendrome(w):
    """divides the word in half and returns false if one half doesn't match the other"""
    for i in range(0, int(len(w)/2)):
        if w[i] != w[len(w)-i-1]:
            return False
        else:
            return True
my_word = 'noon'
print(isPalendrome(my_word))

def is_power(a, b):
    """determines whether a is a power of b"""
    if a % b == 0 and b % (a/b) == 0:
        return True
    else: 
        return False
print(is_power(9, 3))

def gcd(a, b):
    a = int(a)
    b = int(b)
    if a > b:
        c = a - b
        gcd(b, c)
    elif a < b:
        c = b - a
        gcd(a, c)
    # else:
