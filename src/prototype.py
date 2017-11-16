import json
import time
import requests
from contextmanager import ContextManager

URL_BASE = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBLy8qvpCxGo0N1SPMGYaw3WOL5sKfRagE&cx=012303646236362630161:v1nm4ffsvs0&q='
q = 'spain'

#takes in a rest api and return  a list of results
def google(query, url_base = URL_BASE):
	r = requests.get(url_base + query)
	if r.status_code != 200:
		return 'Search Failed!'
	else:
		d = json.loads(r.content)
		return [[x['title'],x['link']] for x in d['items']]

def queryGenerator(lst):
	return '+'.join(lst)

def displayResults(lst,show_topk):
	for t in lst[:min(show_topk,len(lst))]:
		print(t[0])

CONVERSATION_SAMPLE = [
"Do you know about Spain?",\
"That is a big place!",\
"What is the population there?",\
"Now what do you think about France and its problems with Spain",\
"Now what do you think about France and its problems with Spain"
]

#wiki only for the moment

def test():
    contextManager: ContextManager = ContextManager(5)
    for sentence in CONVERSATION_SAMPLE:
    	contextManager.addToContext(sentence)
    	print ('Context:')
    	print (contextManager.getContext())
    	print ('Search Results:')
    	displayResults(google(queryGenerator(contextManager.contextWords)), 3)
    	print('='*20+'\n')

test()