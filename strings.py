fruit = 'banana'
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
    index = 0
    while index < len(word):
        if word[index + place] == letter:
            return index
        index = index + 1
    return -1

print(find('moment', 't', 2))

count = 0 
# for