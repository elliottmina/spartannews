def map(soup, payload, mappings, tag_prop):
	for source_key, payload_key in mappings.items():
		tag = soup.find('meta', attrs={tag_prop:source_key})
		if tag:
			payload[payload_key] = tag.get('content')
