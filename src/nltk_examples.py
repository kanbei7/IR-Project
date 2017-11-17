import nltk

NN = ['NN', 'NNS', 'NNP', 'NNPS', 'NP', 'NPS']
text = nltk.word_tokenize("Do you know information retrieval?")
print([t for t in nltk.pos_tag(text) if t[1] in NN])
