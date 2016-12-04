from nltk.corpus import stopwords
from extractor import extractSonnets
import string
import logging
import numpy as np
from gensim.models import Word2Vec
stop = set(stopwords.words('english')) # for global use

class NNCostFunction(object):

    def __init__(self):
        self.modelName = 'model.txt'
        self.isTrained = False
        self.trainingError = "Model Untrained!"

    # Helper Functions
    # Takes in a sentence, strips punctuation and throws out as list of words
    def splitSentence(sentence):
        sentence_no_punc = sentence.translate(None, string.punctuation)
        words = sentence_no_punc.split()
        return words

    # Takes in a list of words and a stop list, then removes commons words.
    def removeCommonWords(wordList, stopList):
        return filter(lambda word: not (word.lower() in stopList), wordList)

    def trainModel(self):
        sonnets = extractSonnets() #152 Sonnet objects
        sonnet_lines = map(lambda sonnet: map(lambda line: removeCommonWords(splitSentence(line), stop),sonnet.first_twelve), sonnets)
        sonnets_corpus = [word for individual_line in sonnet_lines for word in individual_line]
        model = Word2Vec(sonnets_corpus, min_count=1)
        model.save(self.modelName)
        self.isTrained = True

    def getSimilarityScore(self, word1, word2): # cosine similarity
        if self.isTrained:
            model = Word2Vec.load(self.modelName)
            return model.similarity(word1, word2)
        else:
            print self.trainingError

    def getWordsSimilarTo(self, word): #takes in a single word, can be edited to take more.
        if self.isTrained:
            model = Word2Vec.load(self.modelName)
            return model.most_similar(positive=[word])
        else:
            print self.trainingError

    def generateExamples():
        examples = [
            (('eye', 'sight'), ('shop', 'vile')),
            (('bright', 'fire'),('work', 'lovers')),
            # (('rose', 'flower'),('sweet', 'report')),
            (('beauty', 'love'),('crystal', 'shop'))
        ]
        return examples
