#K-Means Implementation
from nltk.corpus import stopwords
from extractor import extractSonnets
# from sklearn.cluster import KMeans
import string
import sys
import logging
import numpy as np
# import word2vec # for feature extraction
from gensim.models import Word2Vec
stop = set(stopwords.words('english')) # for global use

# Helper Function

# Takes in a sentence, strips punctuation and throws out as list of words
def splitSentence(sentence):
    sentence_no_punc = sentence.translate(None, string.punctuation)
    words = sentence_no_punc.split()
    return words

# Takes in a list of words and a stop list, then removes commons words.
def removeCommonWords(wordList, stopList):
    return filter(lambda word: not (word.lower() in stopList), wordList)

sonnets = extractSonnets() #152 Sonnet objects

sonnet_lines = map(lambda sonnet: map(lambda line: removeCommonWords(splitSentence(line), stop),sonnet.first_twelve), sonnets)
sonnets_corpus = [word for individual_line in sonnet_lines for word in individual_line]
# print sonnet_lines
# sys.exit(0)
# Now we have all the words in all the sonnets, need to get vectorized representation for each word
print "Training model..."
# logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# sentences = [['first', 'sentence'], ['second', 'sentence']]
# train word2vec on the two sentences
min_count = 2
size = 50
window = 4

def join_lst(lst):
    return " ".join(lst)

# print len(sonnets_corpus)
# sys.exit(0)
# corpus = join_lst(map(join_lst, sonnet_lines))
model = Word2Vec(sonnets_corpus, min_count=1)

# model = gensim.models.Word2Vec(sonnet_lines, min_count=1)
model.save('model.txt')
# print "yas"
# print model.similar_by_word('winters')
examples = [
    (('eye', 'sight'), ('shop', 'vile')),
    (('bright', 'fire'),('work', 'lovers')),
    # (('rose', 'flower'),('sweet', 'report')),
    (('beauty', 'love'),('crystal', 'shop'))
]

print "Perfect example: %.5f" % model.similarity('eye', 'eye') # perfect example
print "\n"
for example in examples:
    pos, neg = example
    print "Positive example: %.5f" % model.similarity(pos[0], pos[1])
    print "Negative example: %.5f" % model.similarity(neg[0], neg[1])
    print "\n"
# print model.similarity('shop', 'vile')
# model = word2vec.word2clusters(sonnets_corpus, 'clusters.txt', size=100, True)
