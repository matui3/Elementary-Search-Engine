import re

# this represents a single file in Search Engine

class Document:
    
    # constructs a dictionary which contains the frequency of every term in a document
    def __init__(self, file):
        self._file = file
        self._term_dictionary = {}
        
        with open(file, encoding="utf8") as f:
            tokens = f.read().split()
            for token in tokens:
                token = re.sub(r'\W+', '', token)
                if token not in self._term_dictionary:
                    self._term_dictionary[token] = 1
                else:
                    num = self._term_dictionary[token]
                    num += 1
                    self._term_dictionary[token] = num
        for token in self._term_dictionary.keys():
            val = self._term_dictionary[token]
            self._term_dictionary[token] = 1.0/val

    

    # returns the frequency for a given term
    def term_frequency(self, term):
        if (term in self._term_dictionary):
            return self._term_dictionary[term]
        else:
            return 0

    # provides a list of all words in the document
    def get_words(self):
        words_list = []
        keys = self._term_dictionary.keys()
        for word in keys:
            words_list.append(word)
        return words_list