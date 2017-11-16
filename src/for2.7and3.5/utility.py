def isPOSNoun(tag):
    return tag[:2] == "NN" or tag[:2] == "NP"


def isPOSAdjective(tag):
    return tag[:2] == "JJ"
