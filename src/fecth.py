import json
import time
import requests

url_base = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBLy8qvpCxGo0N1SPMGYaw3WOL5sKfRagE&cx=012303646236362630161:v1nm4ffsvs0&q='
q = 'spain'


#takes in a rest api and return  a list of results
def google(query, url_base):
	r = requests.get(url_base + query)
	if r.status_code != 200:
		return 'Search Failed!'
	else:
		d = json.loads(r.content)
		return [[x['title'],x['link']] for x in d['items']]









