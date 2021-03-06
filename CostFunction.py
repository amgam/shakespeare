from nltk.corpus import stopwords
import nltk
from extractor import extractSonnets
import string
import logging
import os
import numpy as np
from gensim.models import Word2Vec
stop = set(stopwords.words('english')) # for global use


#For Glove use
import itertools
from glove import Corpus, Glove

class Helper(object):
    # Helper Functions

    # Takes in a sentence, strips punctuation and throws out as list of words
    @staticmethod
    def splitSentence(sentence):
        sentence_no_punc = sentence.translate(None, string.punctuation)
        words = sentence_no_punc.split()
        return words

    # Takes in a list of words and a stop list, then removes commons words.
    @staticmethod
    def removeCommonWords(wordList, stopList):
        return filter(lambda word: not (word.lower() in stopList), wordList)

class NNCostFunction(object):

    def __init__(self):
        self.modelName = 'model.txt'
        self.isTrained = False
        self.trainingError = "Model Untrained!"
        self.glove = ""

    # Edited from  https://github.com/okfn/shakespeare/blob/master/contrib/countwords.py
    def shakespeare_words_in_books(self):
        words = []
        for book in nltk.corpus.shakespeare.fileids():
            words.append(nltk.corpus.shakespeare.words(book))
        return words #all the words

    def shakespeare_lines(self):
        with open('shakespeare.txt') as f:
            content = f.readlines()
            return map(lambda line: Helper.removeCommonWords(Helper.splitSentence(line), stop), content)
            # return content

    def trainShake1(self):
        corpus = Corpus()
        shakespeare_words = self.shakespeare_words_in_books()
        # corpus.fit(shakespeare_corpus + sonnets_corpus, window=10)
        corpus.fit(shakespeare_words, window=10)
        self.glove = Glove(no_components=100, learning_rate=0.05)
        self.glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
        self.glove.add_dictionary(corpus.dictionary)

    def trainShake2(self):
        corpus = Corpus()
        shakespeare_words = self.shakespeare_lines()
        # corpus.fit(shakespeare_corpus + sonnets_corpus, window=10)
        corpus.fit(shakespeare_words, window=10)
        self.glove = Glove(no_components=100, learning_rate=0.05)
        self.glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
        self.glove.add_dictionary(corpus.dictionary)

    def trainSonnetsGlove(self):
        corpus = Corpus()
        sonnets = extractSonnets() #152 Sonnet objects
        sonnet_lines = map(lambda sonnet: map(lambda line: Helper.removeCommonWords(Helper.splitSentence(line), stop),sonnet.first_twelve), sonnets)
        sonnets_corpus = [word for individual_line in sonnet_lines for word in individual_line]
        # corpus.fit(shakespeare_corpus + sonnets_corpus, window=10)
        corpus.fit(sonnets_corpus, window=10)
        self.glove = Glove(no_components=100, learning_rate=0.05)
        self.glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
        self.glove.add_dictionary(corpus.dictionary)

    def trainOverallGlove(self):
        corpus = Corpus()
        shakespeare_lines = self.shakespeare_lines()
        sonnets = extractSonnets() #152 Sonnet objects
        sonnet_lines = map(lambda sonnet: map(lambda line: Helper.removeCommonWords(Helper.splitSentence(line), stop),sonnet.first_twelve), sonnets)
        sonnets_corpus = [word for individual_line in sonnet_lines for word in individual_line]

        corpi = shakespeare_lines + sonnets_corpus

        corpus.fit(corpi, window=10)
        self.glove = Glove(no_components=100, learning_rate=0.05)
        self.glove.fit(corpus.matrix, epochs=30, no_threads=4, verbose=True)
        self.glove.add_dictionary(corpus.dictionary)

    def mostSimilarToGlove(self, word, K=10):
        return self.glove.most_similar(word, number=K)

    def trainOverallWord2Vec(self):
        if self.isTrained:
            os.remove(self.modelName)
        shakespeare_words = [word for individual_line in self.shakespeare_words_in_books() for word in individual_line]
        filtered_shakespeare_words = filter(lambda word: word.isalnum(), shakespeare_words)
        shakespeare_corpus = Helper.removeCommonWords(filtered_shakespeare_words, stop)

        sonnets = extractSonnets() #152 Sonnet objects
        sonnet_lines = map(lambda sonnet: map(lambda line: Helper.removeCommonWords(Helper.splitSentence(line), stop),sonnet.first_twelve), sonnets)
        sonnets_corpus = [word for individual_line in sonnet_lines for word in individual_line]

        model = Word2Vec(shakespeare_corpus + sonnets_corpus, min_count=1)
        model.save(self.modelName)
        self.isTrained = True
        print "Training done!"

    def trainOnShakespeareWord2Vec(self):
        if self.isTrained:
            os.remove(self.modelName)
        shakespeare_words = [word for individual_line in self.shakespeare_words_in_books() for word in individual_line]
        filtered_shakespeare_words = filter(lambda word: word.isalnum(), shakespeare_words)
        shakespeare_corpus = Helper.removeCommonWords(filtered_shakespeare_words, stop)
        model = Word2Vec(shakespeare_corpus, min_count=1)
        model.save(self.modelName)
        self.isTrained = True
        print "trainOnShakespeare done!"

    def trainOnSonnetsWord2Vec(self):
        if self.isTrained:
            os.remove(self.modelName)
        sonnets = extractSonnets() #152 Sonnet objects
        sonnet_lines = map(lambda sonnet: map(lambda line: Helper.removeCommonWords(Helper.splitSentence(line), stop),sonnet.first_twelve), sonnets)
        sonnets_corpus = [word for individual_line in sonnet_lines for word in individual_line]
        model = Word2Vec(sonnets_corpus, min_count=1)
        model.save(self.modelName)
        self.isTrained = True
        print "trainOnShakespeare done!"


    def getSimilarityScore(self, word1, word2): # cosine similarity
        if self.isTrained:
            model = Word2Vec.load(self.modelName)
            return model.similarity(word1, word2)
        else:
            print self.trainingError

    def getWordsSimilarTo(self, word, topN): #takes in a single word, can be edited to take more.
        if self.isTrained:
            model = Word2Vec.load(self.modelName)
            return model.most_similar(positive=[word], topn=topN)
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
