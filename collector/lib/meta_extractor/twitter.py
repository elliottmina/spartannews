from lib.meta_extractor import meta_mapper

mappings = {
	'twitter:title':'title',
	'twitter:image:src':'image',
	'twitter:description':'summary',
}

def build(soup, payload):
	meta_mapper.map(soup, payload, mappings, 'name')
