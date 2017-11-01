def mutate(soup):
	paragraphs = get_max_paragraph_set(soup)
	headline = soup.find('h1')

	html = str(headline) + '\n'
	for paragraph in paragraphs:
		html += str(paragraph) + '\n'
	return html

def get_max_paragraph_set(soup):
	paragraph_map = build_paragraph_map(soup)
	key = get_max_key(paragraph_map)
	if key is None:
		raise NoParagraphsError()
	return paragraph_map[key]
	
def get_max_key(paragraph_map):
	max_count = 0
	max_key = None
	for key, paragraphs in paragraph_map.items():
		count = len(paragraphs)
		if count > max_count:
			max_count = count
			max_key = key
	return max_key

def build_paragraph_map(soup):
	paragraph_map = {}
	for paragraph in soup.find_all('p'):
		key = id(paragraph.parent)
		if key not in paragraph_map:
			paragraph_map[key] = []
		paragraph_map[key].append(paragraph)
	return paragraph_map

class NoParagraphsError(RuntimeError):pass
