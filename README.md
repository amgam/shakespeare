# shakespeare
CS221 AI Project on Shakespearean Sonnets


## Cost Functions

Currently the only cost function available is a shallow NN model as implmented via word2vec.

Dependencies include: *nltk and gensim*. These can be installed via
```
pip install -U nltk
pip install --upgrade gensim
```

After NLTK is installed, open up a terminal window and type:
```
python
>>> import nltk
>>> nltk.download()
```

A window should pop up and goto the Corpora tab and scroll down to find `stopwords`. Hit download and you should be good to go.

To use the cost function in your code:
```python
nn = NNCostFunction() # init
nn.trainModel() #IMPT, queries wont work otherwise.

nn.getSimilarityScore(word1, word2) # returns cosine similarity between the two words
nn.getWordsSimilarTo(word, 10) # Returns the top 10 words similar to word. 
nn.generateExamples() # Generates set of examples to work with.
```



