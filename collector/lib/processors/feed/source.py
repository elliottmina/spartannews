import importlib

def build(config):
	return Source(
		config['url'], 
		build_mutators(config, 'rss_mutators'), 
		build_mutators(config, 'html_mutators'))

def build_mutators(config, key):
	if key not in config:
		return []

	return [importlib.import_module(name) for name in config[key]]

class Source():
	def __init__(self, url, rss_mutators, html_mutators):
		self.url = url
		self.rss_mutators = rss_mutators
		self.html_mutators = html_mutators
