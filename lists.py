# importing dependency from exercise 10.8
import random
from datetime import timedelta, datetime

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
print(nest_list)
print('check')
def nested_sum(b):
    ctr = 0
    indices = []
    one_list = []
    i = 0
    for a in b:
        if type(a) is list:
            ctr += 1
            k = b.index(a)
            print(k)
            indices.append(k) # saves the index numbers of the nests
            print(indices)
        else:
            # g = b.pop(a)
            one_list.append(a)
    print(f'one list at this stage is:{one_list}')
    print(f'indices final list is {indices}')

    while i < len(b)-1: # len(b)-1 because i is starting at 0
        print(f'i is: {i}')
        for h in indices:
            print(f'i is: {i}')
            print(b[i])
            print(b.index(b[i]))
            print(h)
            if h == b.index(b[i]):
                # i +=1
                # print(b.pop(i))
                print(b[i])
                p = b.pop(i)
                one_list.extend(p) # adds the popped element to the new list without nesting it
                print(f"one list is now {one_list}")
                i += 1
                # one_list += p
                # print(f"one list is now {one_list}")
            
            
                        # return one_list
                        # return b.pop(i)
            else:
                i += 1
        # i += 1
                                # return False
                                # i += 1
                # one_list.extend(p)
    print(f'one list at the end is:{one_list}')
    return one_list
    return indices # if the result is [0, 2, 3], then the function is saving the indices of the nest correctly
    return ctr # if ctr = 3, then the function is counting all the nests correctly
            
print(nested_sum(nest_list))
new_nest_list = [[1, 2], 3, [4], [5, 6, 7]]
def nested_sum2(b):
    '''returns the sum of a nested list'''
    fin_list = []
    for a in b:
        if type(a) is list:
            fin_list.extend(a)
        else:
            fin_list.append(a)
    return sum(fin_list)
    return fin_list
print(nested_sum2(new_nest_list))

cumulative = [1, 2, 3, 4, 5, 6 , 7, 8, 9, 10]
def cumsum(w):
    '''returns the cumulative sum'''
    i = 0
    sum_cum = []
    for x in w:
        sum_cum.append(x+i)
        i += x
    return sum_cum
print(cumsum(cumulative))

def middle(l):
    '''returns the list minus the first and last elements'''
    return l[1:-1]
myList = [1,2,3,4]
def chop(l):
    '''same function but returns None'''
    l.pop(0)
    l.pop(-1)
    return None

print(chop(myList))
print(myList)

myList = [1, 2, 3, 4]
def is_sorted(l):
    m = sorted(l)
    if l == m:
        return True
    else:
        return False
print(is_sorted(myList))

def is_anagram(word1, word2):
    for letter in word1:
        if letter not in word2:
            return False
        else:
            return True
print(is_anagram('cat', 'table'))


def has_duplicates(l):
    ll = []
    for j in l:
        if j not in ll:
            ll.append(j)
        else:
            return True
        
print(has_duplicates(['t', '4', 't']))

def has_duplicates2(my_list):
    '''alternative solution to has_duplicates (for data structures & algorithms knowledge'''
    i = 0
    while i < len(my_list):
        if my_list.count(my_list[i]) > 1:
            return True
        elif i == (len(my_list) - 1):
            return False
        i += 1

# 10.8
trials = 1000
k = 23
def generate_random_dates(start_date, end_date, k):
    '''generates 23 random birthdays in a class cutoff range'''
    random_dates = []
    date_range = end_date - start_date
    for _ in range(k):
        random_days = random.randint(0, date_range.days)
        random_date = start_date + timedelta(days=random_days)
        random_dates.append(random_date.strftime('%Y-%m-%d')) # appends the birthdays to a list and strips the output so that only a date gets added to the list (no minutes or seconds, etc.)
    return random_dates
start_date = datetime(2019, 9, 1)
end_date = datetime(2020, 8, 31)
random_dates = generate_random_dates(start_date, end_date, 23)
print(f"The random dates generated are:{random_dates}")
# for index, date in enumerate(random_dates):
#     print(f"{index+1}. {date.strftime('%Y-%m-%d')}")
for index, date in enumerate(random_dates):
    print(f"{index+1}. {date}") # prints the list in an easy to read way so I can check the output.

def birthday(days):
    duplicate_count = 0
    for i in range(days):
        if has_duplicates(generate_random_dates(start_date, end_date, k)):
            duplicate_count += 1
    print ("In %d classrooms with %d students, %.1f%% had students\
 with duplicate birthdays." % (trials, k, (float(duplicate_count) / trials) * 100))
print(birthday(trials))

# 10.10

# writing a function that splits a list
# def split_list():

# def in_bisect(word):
#     with open('words.txt') as fd:
#         word_list = fd.read().splitlines()
#     #  possibly need a bested funciton here. 
#     mid = len(word_list)/2
#     # print(mid) # first check. the median of the wordlist was a decimal. 
#     rounded_mid = round(mid)
#     median = word_list[rounded_mid]
#     if word < word_list[rounded_mid]:
#         rounded_mid = rounded_mid/2
#         word_list = word_list[0:rounded_mid]
#         # return True
#     elif word > word_list[rounded_mid]:
#         rounded_mid = rounded_mid/2
#         word_list = word_list[rounded_mid:]
#         # return False
#     else:
#         rounded_mid = rounded_mid/2
#         word_list = word_list[:rounded_mid]
#         # if word in word_list:
#         #     return word_list.index(word)
#         # else:
#         #     return False
    # return word_list[rounded_mid]

def slow_search(word):
    with open('words.txt') as fd: # converts the file into a list
        word_list = fd.read().splitlines()
    if word in word_list:
        return word_list.index(word)
    else:
        return False
print(slow_search('beekeeper'))

def in_bisect(word):
    with open('words.txt') as fd:
        word_list = fd.read().splitlines()
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

print(in_bisect('beekeeper'))
    
