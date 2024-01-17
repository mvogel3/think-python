cheeses = ['Cheddar', 'Edam', 'Gouda']
numbers = [42, 123]
empty = []
print(cheeses, numbers, empty)

numbers[1] = 5 # if I run the file from here, the numbers list will not include 5 because I haven't printed the new list yet. python files run top to bottom.
print(numbers) # now the list shows 5 instead of 123. numbers[1] = 5 replaced rather than appended.
# numbers[2] = 123 will return an error
numbers.append(123) # now the list is [42, 5, 123]
print(numbers)

print("Brie" in cheeses) # good to know that this statement returns True or False. works like jupyter or the normal python interpreter

for i in range(len(numbers)):
    numbers[i] = numbers[i] * 2
print(numbers*4)
print(numbers)
print(numbers+cheeses)

# 10.5 - Slices
t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[:4])
print(t[3:])
print(t[:])

t[1:3] = ['x', 'y'] # replaces 'b' and 'c' with 'x' and 'y'
print(t)

# 10.6 - List Methods
t1 = ['a', 'b', 'c']
t1.append('d')
t2 = ['e', 'f']
t1.extend(t2)
print(t1)
t.sort() # wouldn't run print(t.sort()) because most list methods are void.
print(t)

# 10.7 - Map, Filter, Reduce

def add_all(n):
    '''adds up all the numbers in a list using an augmented assignment statement'''
    total = 0
    for x in n:
        total += x
    return total
print(add_all(numbers))
print(sum(numbers)) # built-in function

def capitalize_all(t):
    '''example of a map function because it "maps" a function onto each element of a list'''
    res = []
    for s in t:
        res.append(s.capitalize())
    return res
print(capitalize_all(cheeses))

sublist = ['back', 'Bone', 'lovely', 'HI']
def only_upper(t):
    '''filter function example. returns a sublist.'''
    res = []
    for s in t:
        if s.isupper(): #isupper() returns true if all characters in a string are uppercase
            res.append(s)
    return res
print(only_upper(sublist))