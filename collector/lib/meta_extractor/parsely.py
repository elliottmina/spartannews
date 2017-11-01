import json
import dateutil.parser
import time

mappings = {
	'author':'author',
	'title':'title',
	'tags':'tags',
	'image_url':'image',
}

def build(soup, payload):
	data = get_data(soup)
	if not data:
		return

	for source_key, payload_key in mappings.items():
		conditional_set(payload, data, source_key, payload_key)

	if 'pub_date' in data:
		date = dateutil.parser.parse(data['pub_date'])
		payload['published'] = time.mktime(date.timetuple())

def get_data(soup):
	parsley = soup.find('meta', attrs={'name':'parsely-page'})
	if parsley:
		content = parsley.get('content')
		return json.loads(content)

def conditional_set(payload, data, source_key, payload_key):
	if source_key in data:
		payload[payload_key] = data[source_key]
