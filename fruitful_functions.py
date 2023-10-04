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

