# my first dictionary

eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp = {'one':'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
# print(eng2sp['four']) (returns an exception)
print(len(eng2sp))

# 11.2
def histogram(s):
    '''counts how many times a letter appears in a string'''
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('brontosaurus')
print(h)
print(h['a'])
print(h.get('a', 0))
print(h.get('c', 0))

def histogram_rewrite(s):
    '''rewrite of histogram using get'''
    d = dict()
    for c in s:
        d[c] = 1 + d.get(c, 0)
    return d
g = histogram_rewrite('parrot')
print(g)

# 11.3
def print_hist(h):
    for c in h:
        print(c, h[c])
print(print_hist(g))

# 11.4 - Reverse Lookup
# v = d[k] (how to find a value from Dictionary d and Key k)

def reverse_lookup(d, v):
    '''takes a value and returns the first key that maps to that value'''
    for k in d:
        if d[k] == v:
            return k
    raise LookupError('value does not appear in dictionary')
key = reverse_lookup(g, 2)
print(key)

# 11.5 - Dictionaries and Lists

def inverse_dict(d):
    '''inverts the keys and values in a dictionary'''
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
            # if val is not in the new dict, we create a new item and initialize it with a singleton
        else:
            inverse[val].append(key)
            # if val is in the new dict already, we append the correspinding key to the existing list
    return inverse
print(inverse_dict(g))

# 11.6 - Memos
known = {0:0, 1:1}
def fibonacci(n):
    '''memorized fibonacci function from chapter 6'''
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res
print(fibonacci(7))
print(known)

# 11.7 - Global Variables
