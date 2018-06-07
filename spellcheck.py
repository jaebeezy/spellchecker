# hw6
# cs435
# created by jae young choi
# spellchecker program

'''
this program utilizes the unix command line
to run: python hw_6.py linux.words (textfile with the sentence to spellcheck)
'''


import re, sys

d = {}
# opening the text file with correct words and creating a hash table
with open(sys.argv[1]) as file:
    for line in file:
        line = line.replace("\n", "")
        line = line.lower()
        d[line] = None

# opening the text file that needs to be spell checked 
with open(sys.argv[2]) as file:
    input_orig = file.read()
    input_orig = input_orig.replace("\n", " ")
input_line = input_orig.lower()
# using regex to remove all puncuation
input_line = re.sub(r'[^\w\s]', '', input_line)
input_list = input_line.split()

# string of all of alphabets for insert and replace functionality
alphabet = 'abcdefghijklmnopqrstuvwxyz'

# swapping each adjacent pair of character in the word
def swap(word):
    word_list = list(word)
    new_word_list = []
    for i in range(len(word_list)):
        if i+1 < len(word_list):
            word_list[i], word_list[i+1] = word_list[i+1], word_list[i]
            new_word = ''.join(word_list)
            new_word = str(new_word)
            word_list[i+1], word_list[i] = word_list[i], word_list[i+1]
            new_word_list.append(new_word)
    return new_word_list

# inserting a letter between each character of the word
def insert(word):
    word_list = list(word)
    new_word_list = []
    for i in range(len(word_list)+1):        
        for letter in alphabet:
            word_list.insert(i, letter)
            new_word = ''.join(word_list)
            new_word = str(new_word)
            word_list.pop(i)
            new_word_list.append(new_word)
    return new_word_list

# deleting a character from the word
def delete(word):
    word_list = list(word)
    new_word_list = []
    for i in range(len(word_list)):
        temp = word_list[i]
        word_list.pop(i)
        new_word = ''.join(word_list)
        new_word = str(new_word)
        word_list.insert(i, temp)
        new_word_list.append(new_word)
    return new_word_list

# replacing each character with a letter in the word
def replace(word):
    word_list = list(word)
    new_word_list = []
    for i in range(len(word_list)):
        temp = word_list[i]
        word_list.pop(i)
        for letter in alphabet:
            word_list.insert(i, letter)
            new_word = ''.join(word_list)
            new_word = str(new_word)
            new_word_list.append(new_word)
            word_list.pop(i)
        word_list.insert(i, temp)
    return new_word_list

# splitting the word into two by a white space 
def split(word):
    word_list = list(word)
    new_word_list = []
    split_word_list = []
    for i in range(len(word_list)):
        if i > 0 and i < len(word_list):
            word_list.insert(i, ' ')
            new_word = ''.join(word_list)
            new_word = str(new_word)
            word_list.pop(i)
            new_word_list.append(new_word)

    for words in new_word_list:
        temp = words.split(' ')
        split_word_list.append(temp)
        
    return split_word_list

# collecting all of the potential candidates of the corrected spelling from all 5 functions
def potentialWords(word):
    potential_words = []
    for a in swap(word):
        if a in d and a not in potential_words:
            potential_words.append(a)
    for b in insert(word):
        if b in d and b not in potential_words:
            potential_words.append(b)
    for c in delete(word):
        if c in d and c not in potential_words:
            potential_words.append(c)
    for e in replace(word):
        if e in d and e not in potential_words:
            potential_words.append(e)
    for f in split(word):
        if f[0] in d and f[1] in d:
            potential_words.append(f[0] + ' ' + f[1])

    # sorting the list of potential words
    potential_words.sort()
    
    for words in potential_words:
        print(words.upper())

# iterating through each word of the input text file and spellchecking
for word in input_list:
    if word not in d:
        print('\n' + input_orig)
        print('word not found: ' + word.upper())
        print('perhaps you meant:')
        potentialWords(word)
        
        

