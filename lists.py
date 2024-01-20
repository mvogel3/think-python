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

print(sublist.pop(1)) # "pops out" one element and deletes the rest of the list
myList = ['howdy', 'there', 'partner', 'I', 'do', 'not', 'know']
del myList[0] # deletes one or more items from a list
print(myList)

s = 'spam'
f = list(s) # breaks a string into individual characters
print(f)

s = 'pining for the fjords'
f = s.split() # built-in method that splits on white space or a specified delimiter
print(f)

s = 'pining-for-the-fjords'
delimiter = '-'
f = s.split(delimiter) 
print(f)
s = delimiter.join(f) # join is the inverse method of split
print(s)

# 10.11 - Aliasing
a = [1, 2, 3]
b = a
print(b is a)
b[1] = 5 # mutating a list (works with aliasing)
print(a)
b = [3, 2, 1] # reassigning value of the variable (does not work with aliasing)
print(a)

# 10.12 - List Arguments
letters = ['a', 'b', 'c']
def delete_head(t):
    del t[0]
    return t
print(delete_head(letters)) # removes 'a' and returns the new list
print(letters) # proves that the list was modified to ['b', 'c']

def bad_delete_head(t):
    t = t[1:]
    return t
    
print(bad_delete_head(letters)) # returns just 'c'
print(letters) # proves that the list was not modified. returns ['b', 'c'] from previous function

def tail(t):
    '''revision of bad_delete_head that appends the 
    divergence of t from letters to a new list'''
    return t[1:] # removes the assignment aspect of bad_delete_head()
rest = tail(letters) # assigns the new list (t) to a new variable called rest
print(rest)

# 10.15 - Exercises
nest_list = [[1, 2], 3, [4], [5, 6, 7]]
print(len(nest_list))
def nested_sum(b):
    ctr = 0
    indices = []
    one_list = []
    i = 0
    for a in b:
        if type(a) is list:
            ctr += 1
            k = b.index(a)
            indices.append(k) # saves the index numbers of the nests
            print(indices)
        else:
            one_list.append(a)
            print(one_list)
            i = 0
            # while i < len(b)-1: # len(b)-1 because i is starting at 0
            for h in indices:
                print(b[i])
                print(h)
                if h == b.index(b[i]):
                    # print(b.pop(i))
                    print(b[i])
                    return b.pop(i)
                else:
                    return False
                    i += 1

                          
                    #     i += 1
                    # return b.pop(i)
                        
                        
    
                    


    # return indices # if the result is [0, 2, 3], then the function is saving the indices of the nest correctly
    # return ctr # if ctr = 3, then the function is counting all the nests correctly
            
print(nested_sum(nest_list))
    # while i < len(b)-1:
    #     if type(a) is list:
    #         ctr += 1
    #         i += 1
    #     else:
    #         i += 1