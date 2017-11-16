from nltk import word_tokenize, pos_tag
from utility import isPOSNoun, isPOSAdjective


class ContextManager(object):
    def __init__(self, contextSize= 5):
        self.contextSize= contextSize
        self.contextWords= []

    @staticmethod
    def _parseContextWords(content):
        contextWords = []
        entities = pos_tag(word_tokenize(content))
        for i in range(len(entities)):
            currentEntity = entities[i]
            currentWord = currentEntity[0]
            currentPOS = currentEntity[1]
            if isPOSNoun(currentPOS):
                contextWord = currentWord
                if i - 1 >= 0:
                    previousEntity = entities[i - 1]
                    previousWord = previousEntity[0]
                    previousPOS = previousEntity[1]
                    if isPOSAdjective(previousPOS):
                        contextWord = previousWord + " " + currentWord
                contextWords.append(contextWord)
        return contextWords

    def addToContext(self, content):
        newContextWords = ContextManager._parseContextWords(content)
        self.contextWords = newContextWords + self.contextWords
        self.contextWords = self.contextWords[:self.contextSize]

    def getContext(self):
        return ' '.join(self.contextWords)
