# AI Project Text Extraction Functions
from sonnet import Sonnet

# Extracts Sonnets from the input text file. Returns a list of 152 Sonnet objects.
# Refer to Sonnet Class for details
def extractSonnets():
    sonnet_collection = []

    with open('sonnets.txt') as reader:
        text = reader.readlines()
        threshold, step_size = 15, 14 # since we have 14 lines

        filtered_text = filter(lambda line: len(line) > threshold, text)
        for i in xrange(0, len(filtered_text), step_size):
            sonnet_collection.append(Sonnet(filtered_text[i:i+step_size]))

        return sonnet_collection

# sonnets = extractSonnets()
