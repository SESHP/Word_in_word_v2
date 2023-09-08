from words import words
from Basic import BasicWord
import random

word = []
subword = []

for i in range(len(words)):
    word.append(words[i]['word'])
    subword.append(words[i]['subwords'])


def load_random_word():
    random_int = random.randint(0, len(word) - 1)
    BW = BasicWord(word[random_int], subword[random_int])
    # print(BW)
    # print(random_int)
    return BW

# load_random_word()
    
def worder(len):
    if len == 1:
        return 'слово'
    if len >= 2 and len <= 4:
        return 'слова'
    if len > 4:
        return 'слов'