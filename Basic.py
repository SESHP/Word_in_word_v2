class BasicWord:
    def __init__(self, word, subword):
        self.word = word
        self.subword = subword
    
    def valid(self, answer):
        return answer in self.subword
    
    def count_subwords(self):
        return len(self.subword)
    
    def __repr__(self):
        return f'{self.subword} от слова {self.word}'
    
class Player:
    def __init__(self, name):
        self.name = name
        self.wordsin = []

    def count_answers(self):
        return len(self.wordsin)
    
    def append_words(self, word):
        self.wordsin.append(word)
    
    def uset_word(self, word):
        # print(self.wordsin)
        return word in self.wordsin
    
    def __repr__(self):
        return f'{self.name} - {self.wordsin}'
        

