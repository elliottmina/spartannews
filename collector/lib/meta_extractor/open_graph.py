from lib.meta_extractor import meta_mapper

mappings = {
	'og:site_name': 'site',
	'og:title': 'title',
	'og:image': 'image',
	'og:description': 'summary',
}

def build(soup, payload):
	meta_mapper.map(soup, payload, mappings, 'property')
