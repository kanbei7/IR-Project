import json
import requests
import urllib

s1='https://en.wikipedia.org/w/api.php?action=query&prop=extracts&exintro=&exsentences=2&explaintext=true&redirects=&formatversion=2&&format=json&'
URL_BASE = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBLy8qvpCxGo0N1SPMGYaw3WOL5sKfRagE&cx=012303646236362630161:v1nm4ffsvs0&q='
q = 'spain'

def urlEncoding(s):
	return urllib.urlencode({'titles':s[:(len(s)-12)]})

def saveRes(d,fname):
	json.dump(d,open(fname+'.json','w'))
	with open(fname+'.txt','w') as f:
		f.writelines(d['query']['pages'][0]['extract'].encode('utf-8'))

def saveTitles(l):
	with open('titles.txt','w') as f:
		f.writelines(','.join(l))

def getRes(t , fname):
	q = urlEncoding(t)
	r = requests.get(s1 + q)
	d = json.loads(r.content)
	saveRes(d,fname)


r = requests.get(URL_BASE + q)
d = json.loads(r.content)
l = [x['title'] for x in d['items']]

saveTitles(l)


for i in range(len(l)):
	fname = 'top%d'%i
	getRes(l[i] , fname)

