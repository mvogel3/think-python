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
    for w in word:
        if w in forbidden:
            return False
    return True
# print(avoids('aware','jkiw'))

def uses_only(word, only):
    for w in word:
        if w not in only:
            return False
    return True
print(uses_only('exact', 'tacex'))

def uses_all(word, only):
    return(uses_only(only, word))