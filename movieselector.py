import requests
import bs4 
import json
import random

def movieselector(imdb_url):
	res = requests.get(imdb_url)
	res.raise_for_status()
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	js_elements = soup.find_all('script')
	js_text = None
	search_str = 'IMDbReactInitialState.push('

	for element in js_elements:
	    text = element.text
	    if search_str in text:
	        js_text = text.strip()
	        break

	json_start = js_text.index(search_str) + len(search_str)
	json_text = js_text[json_start:-2]
	json_obj = json.loads(js_text[json_start:-2])
	imdb_lista = []
	for title in json_obj['titles']:
	    json_title = json_obj['titles'][title]
	    imdb_lista.append(json_title['primary']['title'])

	random_movie = random.choice(imdb_lista)
	return random_movie