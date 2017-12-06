import json
import requests
import urllib
from src.contextmanager import ContextManager

URL_BASE = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBLy8qvpCxGo0N1SPMGYaw3WOL5sKfRagE&cx=012303646236362630161:v1nm4ffsvs0&q='
q = 'spain'

s1='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&exsentences=2&explaintext=true&redirects=&formatversion=2&&format=json&'


chatbot_key = '0aa8e9a6-aec5-4988-a58f-80867b8f0df6'
chatbot_url = 'http://sandbox.api.simsimi.com/request.p?key='+'0aa8e9a6-aec5-4988-a58f-80867b8f0df6'+'&lc=en&ft=1.0&'

# takes in a rest api and return  a list of results
def google(query, url_base=URL_BASE):
    r = requests.get(url_base + query)
    if r.status_code != 200:
        return 'Search Failed!'
    else:
        d = json.loads(r.content)
        return [[x['title'], x['link']] for x in d['items']]

def saveRes(d,fname):
    json.dump(d,open(fname+'.json','w'))
    with open(fname+'.txt','w') as f:
        f.writelines(d['query']['pages'][0]['extract'].encode('utf-8'))

def urlEncoding(s):
    return urllib.parse.urlencode({'text':s})

def urlEncoding2(s):
    return urllib.parse.urlencode({'titles':s})

def getRes(t):
    q = urlEncoding2(t)
    r = requests.get(s1 + q)
    d = json.loads(r.content)
    print(d['query']['pages'][0]['extract'].encode('utf-8'))

def queryGenerator(lst):
    return '+'.join(lst)

def displayResults(lst, show_topk):
    for t in lst[:min(show_topk, len(lst))]:
        title = t[0][:(len(t[0])-12)]
        print(title)
        print(getRes(title))
        print(t[1])

'''
CONVERSATION_SAMPLE = [
    "Do you know about Spain?",
    "That is a big place!",
    "What is the population there?",
    "Now what do you think about France and its problems with Spain",
    "Now what do you think about France and its problems with Spain"
]
'''

# more weight to new words
# wiki only for the moment

def display(s, c):
    c.addToContext(s)
    print('-' * 10)
    #print('Context:')
    #print(c.getContext())
    #print('+' * 10)
    print('Search Results:')
    displayResults(google(queryGenerator(c.contextWords)), 3)
    print('=' * 20 + '\n')


def test():
    c = ContextManager(5)
    for sentence in CONVERSATION_SAMPLE:
        display(sentence, c)


def reaction(s):
    q = chatbot_url+urlEncoding(s)
    r = requests.get(q)
    return json.loads(r.content)['response']

def interactive_test():
    c = ContextManager(5)
    while True:
        x = input("You: \n")
        print ("Deafult Cahtbot: ")
        print(reaction(x))
        print('+'*10)
        display(x.strip(), c)


# test()

# interactive test
interactive_test()
