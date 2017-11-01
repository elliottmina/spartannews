def build(soup, payload):
	build_link(soup, payload)
	build_summary(soup, payload)
	build_tags(soup, payload)

def build_link(soup, payload):
	tag = soup.find('link', rel="canonical")
	if tag:
		payload['id'] = tag.get('href')
		payload['url'] = tag.get('href')

def build_summary(soup, payload):
	tag = soup.find('meta', attrs={'name':'description'})
	if tag:
		payload['summary'] = tag.get('content')

def build_tags(soup, payload):
	tag = soup.find('meta', attrs={'name':'keywords'})
	if tag:
		payload['tags'] = tag.get('content')

