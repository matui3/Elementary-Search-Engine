import math
import os
import re
from document import Document


class SearchEngine:

    # constrcuts an inverse index 
    def __init__(self, dir):
        # inverse index (dictionary which maps terms to list of documents)
        self._docs = {}
        self._doc_list = []
        self._dir_name = dir
        for file in os.listdir(dir):
            # creates a list of every document in the directory
            pathname = dir + '/' + file
            self._doc_list.append(pathname)
            # below represents a dictionary which contains all of the term frequencies for words
            doc = Document(pathname)
            # grabs list of words in the document, if the word is not in the dictionary, then add it as a list
            for word in doc.get_words():
                if word not in self._docs:
                    doc_list = [file]
                    self._docs[word] = doc_list
                else:
                    doc_list = self._docs[word]
                    doc_list.append(file)
    
    # calculate inverse document frequency, takes term as string argument and returns score for that term over all documents
    def _calculate_idf(self, term):
        term = term.lower()
        term = re.sub(r'\W+', '', term)
        if term in self._docs:
            total_docs = len(self._doc_list)
            num_docs_with_term = len(self._docs[term])
            return math.log(total_docs/num_docs_with_term)
        else:
            return 0.0
        
    def search(self, term):
        TF_IDF_list = []
        # self._docs is the dictionary which contains all the word present in the all documents
        term = term.lower()
        term = re.sub(r'\W+', '', term)
        if term in self._docs:
            documents = self._docs[term] # list of all documents with the given term
            # calculate TFIDF per document
            for document in documents:
                dir = self._dir_name
                pathname = dir + '/' + document
                doc = Document(pathname)               
                term_freq = doc.term_frequency(term)
                inv_doc_freq = self._calculate_idf(term)
                TF_IDF = term_freq * inv_doc_freq
                score = (pathname, TF_IDF)
                TF_IDF_list.append(score)
            TF_IDF_list = sorted(TF_IDF_list, key=lambda score: score[1], reverse=True)
            print(TF_IDF_list)
            doc_list = []
            for doc in TF_IDF_list:
                doc_list.append(doc[0])
            return doc_list
        else:
            return None
