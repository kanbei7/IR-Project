def isPOSNoun(tag: str) -> bool:
    return tag[:2] == "NN" or tag[:2] == "NP"


def isPOSAdjective(tag: str) -> bool:
    return tag[:2] == "JJ"
