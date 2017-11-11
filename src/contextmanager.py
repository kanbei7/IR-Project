from typing import List, Tuple
from nltk import word_tokenize, pos_tag

from src.utility import isPOSNoun, isPOSAdjective


class ContextManager(object):
    def __init__(self, contextSize: int = 5):
        self.contextSize: int = contextSize
        self.contextWords: List[str] = []

    @staticmethod
    def _parseContextWords(content: str) -> List[str]:
        contextWords: List[str] = []
        entities: List[Tuple[str, str]] = pos_tag(word_tokenize(content))
        for i in range(len(entities)):
            currentEntity: Tuple[str, str] = entities[i]
            currentWord: str = currentEntity[0]
            currentPOS: str = currentEntity[1]
            if isPOSNoun(currentPOS):
                contextWord: str = currentWord
                if i - 1 >= 0:
                    previousEntity: Tuple[str, str] = entities[i - 1]
                    previousWord: str = previousEntity[0]
                    previousPOS: str = previousEntity[1]
                    if isPOSAdjective(previousPOS):
                        contextWord: str = previousWord + " " + currentWord
                contextWords.append(contextWord)
        return contextWords

    def addToContext(self, content: str) -> None:
        newContextWords: List[str] = ContextManager._parseContextWords(content)
        self.contextWords = newContextWords + self.contextWords
        self.contextWords = self.contextWords[:self.contextSize]

    def getContext(self) -> str:
        return ' '.join(self.contextWords)
