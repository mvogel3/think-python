# fin = open('words.txt')
# print(fin.readline())
# for line in fin:
#     print(line)
# words_list = []
# for line in fin:
#     words = line.strip()
#     words_list.append(words)

# write a program that reads words.txt and prints only the words with more than 20 characters
def twenty_something():
    fin = open('words.txt')
    word_list = []
    for line in fin:
        char_count = len(line)
        if char_count > 20:
            word_list.append(line)
    return word_list

# print(twenty_something())

def has_no_e(word):
    for letter in word:
        if letter =='e':
            return False
    return True
# print(has_no_e('exact'))

def words_without_e():
    new_fin = open('words.txt')
    word_list = []
    no_e_list = []
    for l in new_fin:
        # print(l)
        word_list.append(l)
        if has_no_e(l) ==True:
            # print(l)
            no_e_list.append(l)
    return len(no_e_list)/len(word_list)

# print(words_without_e())

def avoids(word, forbidden):
    '''returns true if the word does not contain any forbidden letters'''
    for w in word:
        if w in forbidden:
            return False
    return True
# print(avoids('aware','jkiw'))

def uses_only(word, only):
    '''returns true if the word uses only the letters in only'''
    for w in word:
        if w not in only:
            return False
    return True
# print(uses_only('exact', 'tacex'))

def uses_all(word, only):
    '''returns true if the word uses all of the letters in only at least once 
    (use-case of uses_only)'''
    return(uses_only(only, word))

def is_abecedarian(word):
    '''returns true if the letters in the word are in alphabetical order 
    (double letters are okay)'''
    previous = word[0]
    for c in word:
        if c < previous:
            return False
        previous = c 
        # what does this line do? makes it so that c becomes the next letter and each 
        # iteration is comparing a different letter? otherwise everything is 
        # compared to the first letter.
    return True

# print(is_abecedarian('lotty'))

def is_abecedarian2(word):
    '''same function but using recursion'''
    if len(word) <= 1:
        return True
    # because the "word" is alphabetical if it only has one letter
    if word[0] > word[1]:
        return False
    return is_abecedarian2(word[1:])
# moves onto to the second letter and passes the word through the function again minus the 
# previous letter. if at any point, the new first letter is greater than the new second, 
# the function returns false and the recursion stops. 

# print(is_abecedarian2('lotty'))

def is_abecedarian3(word):
    i = 0
    while i < len(word)-1:
        # len(word)-1 because i starts at 0 and will be 1 letter less than the real length 
        # by the end of the loop.
        if word[i+1] < word[i]:
            return False
        i = i+1
    return True

# print(is_abecedarian3('lotty'))

def is_palendrome(word):
    '''version of the palendrome funciton using indices'''
    i = 0
    j = len(word)-1
    while i < j:
        if word[i] != word[j]:
            return False
        i = i + 1
        j = j - 1
    return True

# exercises

# def three_doubles():
#     fin = open('words.txt')
#     word_list = []
#     for line in fin:
#         i = 0
#         char_count = len(line)
#         while i < char_count-1:
#             if char_count[i+1] != char_count[i]:

#         i = i + 1
                

#         if char_count > 20:
#             word_list.append(line)
#     return word_list

def three_doubles_works(word):
    '''this function returns true for three double letters but not consecutive double letters'''
    i = 0
    j = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            j = j + 1
            print(j)
        i = i + 1
    if j == 3:
        return True

print(three_doubles_works('mississippi'))

def three_doubles(word):
    '''this function returns true for three double letters but not consecutive double letters'''
    i = 0
    j = 0
    while i < len(word)-1:
        if word[i] == word[i+1] and word[i+2] == word[i+3] and word[i+4] == word[i+5]:
            j = j + 1
            print(j)
        i = i + 1
    if j == 3:
        return True
    
# print(three_doubles('mississippi'))

def doubles_recursion(word):
    '''function returns true for three consecutive double letters but only if '''
    if word[0] == word[1] and word[2] == word[3] and word[4] == word[5]:
        return True
    elif word[0] != word[1]:
        return doubles_recursion(word[1:])
    else:
        return False

print(doubles_recursion('abcmmssii'))

def doubles_recursions(word):
    j = 0
    previous = word[0]
    if j == 3:
        return True
    for w in word:
        if w == previous:
            j = j + 1
        previous = w
        
      
                