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

def three_doubles_works(word):
    '''this function returns true for three double letters but not consecutive double letters'''
    i = 0
    j = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            j = j + 1
        i = i + 1
    if j == 3:
        return True

print(three_doubles_works('mississippi'))

def find_double(word):
    '''github solution that perfects the three_doubles_works function
    I was working on. '''
    i = 0
    ctr = 0 
    while i < len(word) - 2:
        if word[i+1] == word[i]:
            ctr += 1
            i += 2
            if ctr == 3:
                return word
            else:
                ctr = 0
                i += 1
    return None

def doubles_recursion(word):
    '''function returns true for three consecutive double letters using recursion'''
    if len(word) <= 6:
        return False
    elif word[0] == word[1] and word[2] == word[3] and word[4] == word[5]:
        return True
    elif word[0] != word[1]:
        return doubles_recursion(word[1:])
    else:
        return False

print(doubles_recursion('forgetfulness'))

def three_doubles():
    fin = open('words.txt')
    consecutive_list = []
    for line in fin:
        if doubles_recursion(line) == True:
            consecutive_list.append(line)
    return consecutive_list

print(three_doubles()) 

def odometer_palindrome():
    palendrome_list = []
    for i in range(100000, 1000000): # 100K to 1m not including 1m
        i = str(i) # transforms each integer i to a string so that they can be sliced by index
        if is_palendrome(i[2:6]) == True:
            palendrome_list.append(i)
        if is_palendrome(i[1:6]) == True:
            palendrome_list.append(i)
        if is_palendrome(i)==True:
            palendrome_list.append(i)     
    print(len(palendrome_list))
    return palendrome_list
# print(odometer_palindrome())

def age_palendrome():
    diff = 15
    while diff < 50:
        ctr = 0
        my_age = 0
        while my_age < 99:
            parent_age = my_age + diff



    
        if is_palendrome(my_age) == parent_age:
            ctr += 1
        else:
            diff += 1
    