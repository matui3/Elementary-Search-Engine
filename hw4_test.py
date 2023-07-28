from cse163_utils import assert_equals

from document import Document
from search_engine import SearchEngine
    
def test_document_constructor():
    doc = Document('word_tests/words.txt')
    print(doc.get_words())
    print(doc.term_frequency('cutest'))


def test_search_engine_constructor():
    test = SearchEngine('hw4/word_tests')
    print(test)

def test_search_function():
    engine = SearchEngine('word_tests')
    return engine.search('cutest')

def test_search_idf():
    engine = SearchEngine('word_tests')
    return engine._calculate_idf('cutest')

def main():
    # test_document_constructor()
    # test_search_engine_constructor()
    print(test_search_function())
    # print(test_search_idf())


if __name__ == '__main__':
    main()