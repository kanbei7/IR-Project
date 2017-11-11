import nltk

# make sure the following commands are executed at the first time
# nltk.download('maxent_treebank_pos_tagger')
# nltk.download('averaged_perceptron_tagger')

NN = ['NN', 'NNS', 'NNP', 'NNPS', 'NP', 'NPS']
text = nltk.word_tokenize("Do you know information retrieval?")
print([t for t in nltk.pos_tag(text) if t[1] in NN])
