import json
import dateutil.parser
import time
from pprint import pprint

def build(soup, payload):
	script = soup.find('script', type="application/ld+json")
	if not script:
		return

	try:
		data = json.loads(script.get_text())
	except json.JSONDecodeError:
		return

	build_published(payload, data)
	build_author(payload, data)
	build_title(payload, data)
	build_image(payload, data)
	build_site(payload, data)

def build_published(payload, data):
	key = get_published_key(data)
	if not key: 
		return

	date = dateutil.parser.parse(data[key])
	payload['published'] = time.mktime(date.timetuple())

def get_published_key(data):
	for key in ['dateModified', 'datePublished','dateCreated',]:
		if key in data:
			return key

def build_author(payload, data):
	if 'author' not in data:
		return

	author = data['author']

	if isinstance(author, str):
		payload['author'] = author

	if isinstance(author, list):
		author = author[0]

	if 'name' in author:
		payload['author'] = author['name']

def build_title(payload, data):
	if 'headline' in data:
		payload['title'] = data['headline']

def build_image(payload, data):
	if 'image' in data and 'url' in data['image']:
		payload['image'] = data['image']['url']

def build_site(payload, data):
	if 'publisher' in data and 'name' in data['publisher']:
		payload['site'] = data['publisher']['name']
