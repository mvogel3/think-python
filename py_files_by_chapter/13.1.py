import string
# print(string.punctuation)
# print(string.whitespace)

def StripWords(file):
    for line in file:
        translator = line.maketrans('', '', string.punctuation)
        words = line.translate(translator).lower().strip().replace(" ", "")
    return words
    
print(StripWords('Howdy YHD(h:      dwniofe ^'))
# print(StripWords(open('words.txt')))

