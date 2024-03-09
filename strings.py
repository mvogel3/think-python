fruit = 'banana'
i = 1
fruit[i+1]
# index starts at 0
letter = fruit[0]
length = len(fruit)
last = fruit[length - 1]
print(last)

index = 0
while index < len(fruit):
    letter = fruit[index]
    print(letter)
    index = index + 1
# why use a while loop instead of a for loop? use cases?
for letter in fruit:
    print(letter)

prefixes = 'JKLMNOPQ'
suffix = 'ack'
for letter in prefixes:
    if letter == 'Q' or letter == 'O':
        letter = letter + 'u'
        print(letter + suffix)
    else:
        print(letter + suffix)

s = 'Monty Python'
# 0 through 5 not including 5
print(s[0:5])
print(s[5:6]) # printing the space in the string
print(s[6:12])  


def find(word, letter, place):
    '''returns the index of a letter. place argument added for repeat letters or to clarify 
    where in the index to start finding'''
    index = 0
    while index < len(word):
        if word[index + place] == letter:
            return index
        index = index + 1
    return -1

print(find('moment', 'm', 2))

# first instance of a counter in the textbook. counts the number of 'a's in 'banana'
count = 0 
for letter in fruit:
    if letter == 'a':
        count = count + 1
print(count)

def count(word, letter):
    counter = 0
    # need an iterator different from the argument in order for the function to work. 
    # i.e. letter can't equal letter
    for l in word:
        if l == letter:
            counter = counter + 1
    return counter
print(count('banana', 'a'))

print(fruit.upper())

def in_both(word1, word2):
    """returns a list of all the letters two words have in common"""
    letters = []
    for letter in word1:
        if letter in word2:
            letters.append(letter)
    return letters
print(in_both('apples', 'oranges'))

print(fruit.count('n'))

print(fruit[0:5:2])

def isPalendrome(w):
    """shortened version of palendrome function using a Python string method"""
    if w[::-1]:
        return True

print(isPalendrome('hannah'))

def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False
        
def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'
        
def any_lowercase3(s):
    # flags = []
    for c in s:
        flag = c.islower()
        # flags.append(flag)
    return flag

def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
        # flags.append(flag)
    return flag
        
any_lowercase4('haNnah')

# 8.5
def rotate_word(s, i):
    '''came back to write this for chapter 11. the list comprehension is from wikipedia'''
    for abcd in ["abcdefghijklmnopqrstuvwxyz", "ABCDEFGHIJKLMNOPQRSTUVWXYZ"]:
        s = ''.join([abcd[(abcd.index(char) + i) % 26] if char in abcd else char for char in s])
    return s

print(rotate_word('melon', -10))
