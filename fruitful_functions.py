import math

# in the function below, "a" is a temporary variable
def area(radius):
    a = math.pi * radius**2
    return a
print(area(4))

def compare(x, y):
    if x > y:
        return "1"
    if x == y:
        return "0"
    if x < y:
        return "-1"
    
print(compare(3, 7))

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    
print(absolute_value(-6))