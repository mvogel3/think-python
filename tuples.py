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