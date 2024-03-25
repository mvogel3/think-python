# dependencies for generating random integer values in Exercise 11.4
from random import seed
from random import randint

# my first dictionary

eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp = {'one':'uno', 'two': 'dos', 'three': 'tres'}
print(eng2sp)
# print(eng2sp['four']) (returns an exception)
print(len(eng2sp))

# 11.2 - Dictionary as a Collection of Counters
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

# 11.10 - Exercise

# 11.1
def words_dict():
    '''reads word.txt and assigns the lines as keys in a dictionary'''
    with open('words.txt') as fin:
        lines = fin.read().splitlines()#[0:10]
    word_dict = dict()
    c = 0
    for word in lines:
        word_dict[word] = c + 1
        c += 1
    return word_dict
# print(words_dict())
def lookup(k):
    word_dict = words_dict()
    v = word_dict[k]
    if k in word_dict:
        return v
print(lookup('aa'))

# 11.2
def set_invert(d):
    inverse = dict()
    for key in d:
        val = d[key]
        inverse.setdefault(val, []).append(key)
    return inverse
print(set_invert(g))

# 11.3
memo_ack = {0:{0:1, 1:2, 2:3}, 1:{0:2, 1:3}, 2:{0:3, 1:5}}
def ack(m, n):
    """ackermann function (from chapter 6)"""
    if m in memo_ack.keys() and n in memo_ack[m].keys():
        return memo_ack[m][n]
    else:
        if m == 0:
            res = n + 1
        if m > 0 and n == 0:
            res = ack(m-1, 1)
        if m > 0 and n > 0:
            res = ack(m-1, ack(m, n-1))
    memo_ack.setdefault(m,{}).setdefault(n,res)
    return res
    
print(ack(3,4))
# print(memo_ack)
# import sys
# print(sys.getrecursionlimit())

# 11.4
def old_has_duplicates(my_list):
    '''has_duplicates function from chapter 10.7'''
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1

def has_duplicates(my_list):
    '''new duplicate search function using a dictionary'''
    items = dict()
    for l in my_list:
        items[l] = 1 + items.get(l, 0)
    for i in items:
        if items[i] >= 2:
            return True
        else:
            return False  
print(has_duplicates(['t', '4', 't']))

# 11.5
def rotate_word(s, i):
    '''from chapter 8'''
    for abcd in ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
        s = ''.join([abcd[(abcd.index(char) + i) % 26] if char in abcd else char for char in s])
    return s
# print(rotate_word('aa',0))

def in_bisect(word, word_list):
    # with open('words.txt') as fd:
    #     word_list = fd.read().splitlines()
    lo = 0
    hi = len(word_list)
    while lo < hi:
        mid = (lo + hi)//2 # approximate midpoint. ensures mid is an integer
        if word_list[mid] < word:
            lo = mid + 1
        else:
            hi = mid
    if word != word_list[hi]:
        return None
    else:
        return lo
# print(in_bisect('xx'))
import bisect as bs

def exist_check(a, x):
    '''
	Checks if a is in x.
	a: string
	x: list
	
	Returns: bool
	'''
	#https://docs.python.org/2/library/bisect.html
    i = bs.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False


cypher = {}
def rotate_pairs():
    pairs = dict()
    with open('words.txt') as fin:
        lines = fin.read().splitlines()#[0:10]
    # rotator = randint(0, 10)
    # print(rotator)
    for l in lines:
        for i in range(1, 26): #could also do range(-25,25) but i dont care to mess with this function again
            r = rotate_word(l, i)
            # print(i)
            if exist_check(lines, r) == True:
                pairs[l] = r
                cypher.setdefault(l,{}).setdefault(i,r) # naturally the index error was an indent error on my part lol
            # should the second key be the rotator number or the rotated word?
    return len(pairs)


print(rotate_pairs())
print(cypher)
# def find_rot_pairs():
#     final_list = []
#     for word in word_dict:
#         for i in range(1, 26):
#             if rotate.rotate_word(word, i) in word_dict:
#                 final_list.append((word, i, rotate.rotate_word(word, i)))
#     final_list.sort()
#     for pair in final_list:
#         print pair

# find_rot_pairs()

# the two commented lines below are for using nested dictionaries as memos.
        # if l in cypher.keys() and rotator in cypher[l].keys():
        #     return cypher[l][rotator]

# seed random number generator
# seed(1)
# generate some integers
# for _ in range(10):
# 	value = randint(0, 10)
# 	print(value)

# 11.6
