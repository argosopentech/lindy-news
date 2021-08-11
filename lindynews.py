import csv
from collections import defaultdict

headlines_file = open('headlines.csv')
reader = csv.reader(headlines_file)


# Dictionary word -> total count of word
word_count = defaultdict(int)

# word -> lindy sum
lindy_count = defaultdict(int)

for date, headline, is_lindy in reader:
    is_lindy = int(is_lindy) > 0
    words = headline.split(' ')
    for word in words:
        word_count[word] += 1
        if is_lindy:
            lindy_count[word] += 1

def lindy_of_word(word):
    if word_count[word] == 0 or lindy_count[word] == 0:
        return 0.0
    else:
        return float(lindy_count[word]) / word_count[word]

def lindy_of_headline(headline):
    words = headline.split(' ')
    return sum([lindy_of_word(word) for word in words]) / len(words)

LINDY_THRESHOLD=0.1

def is_lindy(headline):
    return lindy_of_headline(headline) >= LINDY_THRESHOLD

while True:
    i = input()
    l = is_lindy(i)
    if l:
        print('Lindy')
    else:
        print('Not Lindy')
    

