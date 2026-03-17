from nltk.parse import CoreNLPParser
from nltk.tokenize import word_tokenize

standfordnertagger = CoreNLPParser(url='http://localhost:9000', tagtype='ner')

def tag(txt):
    toponyms = set()
    toponym = []

    for word, tag in standfordnertagger.tag(word_tokenize(txt)):
        if tag == 'LOCATION':
            toponym.append(word)
        elif toponym:
            toponyms.add(" ".join(toponym).lower())
            toponym = []
    return toponyms

if __name__ == '__main__':
    print(tag('There was once a man in Amsterdam who tweeted about a Flood in Texas'))
