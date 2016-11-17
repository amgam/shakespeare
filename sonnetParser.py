from nltk import pos_tag, word_tokenize
from nltk.corpus import cmudict
import string
import extractor

sylDict = cmudict.dict()

def num_syllables(word):
        return [len(list(y for y in x if y[-1].isdigit())) for x in sylDict[word.lower()]] 


def guess_num_syllables(sylLeft, unknowns, result):
    totalLen = sum([len(unknown) for unknown in unknowns])
    for word, pos in unknowns:
        result[pos][word]["numSyl"] = int(round((float(len(unknown))/float(totalLen)) * float(sylLeft)))
        if result[pos][word]["numSyl"] <= 0:
            result[pos][word]["numSyl"] = 1


def parse_sonnets():
    sonnets = extractor.extractSonnets()
    result = dict()
    count = 0
    for sonnet in sonnets:
        for line in sonnet.sonnet_text:
            sylLeft = 10
            unknowns = set()
            for upperWord, partOfSpeech in pos_tag(word_tokenize(line)):
                if upperWord in string.punctuation:
                    continue
                word = upperWord.lower()
                if partOfSpeech not in result:
                    result[partOfSpeech] = dict()
                if word not in result[partOfSpeech]:
                    result[partOfSpeech][word] = dict()
                    if word in sylDict:
                        result[partOfSpeech][word]["numSyl"] = num_syllables(word)[0]
                        sylLeft -= result[partOfSpeech][word]["numSyl"]
                    else:
                        unknowns.add((word, partOfSpeech))
                elif "numSyl" in result[partOfSpeech][word]:
                    sylLeft -= result[partOfSpeech][word]["numSyl"]
            guess_num_syllables(sylLeft, unknowns, result)
            count += 1
    for pos in result:
        count = 0
        sylSum = 0
        for word in result[pos]:
            count += float(1)
            sylSum += float(result[pos][word]["numSyl"])
        result[pos]["AVERAGE_TOKEN"] = float(sylSum/count)
    return result

