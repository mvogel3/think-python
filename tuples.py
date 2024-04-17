my_first_tuple = ('a', 'b', 'c', 'd', 'e')

my_second_tuple = tuple('lupins')
print(my_second_tuple[2])

# NEED to include the comma when replacing/concatenating a tuple.
my_first_tuple = ('A',) + my_first_tuple[1:]
print(my_first_tuple)

# 11.2 - Tuple Assignment
a, b = 1, 2
print(a)
a, b = b, a
print(a)

addr = 'monty@python.org'
uname, domain = addr.split('@')
print(uname, domain)

# 11.3 - Tuples as Return Values
t = divmod(7, 3) # saves quotent and remainder seperately in a tuple
print(t)
quote, rem = divmod(7, 3) # saves quotient and remainder to two different tuples
print(quote, rem)

def min_max(t):
    return min(t), max(t)
print(min_max(t))

# 12.4 - Variable-length argument tuples
def sum_all(*args):
    '''uses the * parameter to gather arguments into a tuple'''
    return sum(args)
print(sum_all(1,2,3))

# 12.5 - Lists and tuples
s = 'abc'
t = [0, 1, 2]
for pair in zip(s,t):
    print(pair)
print(list(zip(s,t))) # the result is a list of tuples

print(list(zip('Anne', 'Elk'))) # if the sequences are not the same length, 
# the result is the length of the shorter one. 

t = [('a', 0), ('b', 1), ('c', 2)]
# uses tuple assignment in a for loop to traverse a list of tuples
for letter, number in t:
    print(letter, number)

def has_match(t1, t2):
    '''traverses two (or more) sequences and returns True if there is an index i
    such that t1[i] == t2[i]'''
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

# traverses the elements of a sequence and their indices using the built-in enumerate function
for index, element in enumerate('abc'):
    print(index, element) 

# 12.6 - Dictionaries and tuples
d = {'a':0, 'b':1, 'c':2}
# making a dictionary from a tuple
t = d.items()
print(t)

for key, value in d.items():
    print(key, value)

# making a tuple from a dictionary
t = [('a', 0), ('c', 2), ('b', 1)]
d = dict(t)
print(d)

# more concise way to make a dictionary
d2 = dict(zip('abcefg', range(6)))
print(d2)

# 12.8 - Debugging
# importing the structshape file which summarizes the "shape" of the data structure
from structshape import structshape 
t = [1,2,3]
print(structshape(t))

t2 = [[1,2], [3,4], [5,6]]
print(structshape(t2))

# if the elemeents of the list are not the same type, structshape groups them, in order, by type.
t3 = [1,2,3,4.0,'5','6',[7],[8],9]
print(structshape(t3))

# list of tuples
s = 'abc'
lt = list(zip(t,s))
print(lt)
print(structshape(lt))

# dictionary with 3 items that map integers to strings
d = dict(lt)
print(d)
print(structshape(d))

# 12.10 - Exercises
