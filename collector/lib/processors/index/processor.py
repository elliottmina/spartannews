import requests

from lib.util.mutate import mutate
from lib.meta_extractor import meta_extractor
from lib.util import errors
from lib.util import output

def get_urls(source):
	content = requests.get(source.url).text
	return mutate(source.index_mutators, content)

def build_payload(source, url):
	html = requests.get(url).text

	meta = meta_extractor.extract(html)
	meta['content'] = mutate(source.html_mutators, html)
	meta['id'] = url
	meta['url'] = url

	return meta

class Processor:
	def __init__(self, filters):
		self.filters = filters

	def process(self, upserter, source):
		[self.process_url(upserter, source, url) for url in get_urls(source)]

	def process_url(self, upserter, source, url):
		try:
			print('> Processing "{}"'.format(url))
			payload = build_payload(source, url)
			upserter.upsert(payload)
		
		except Exception as e:
			errors.add_exception(e)
			output.submessage(errors.errors[-1]['message'])
			[output.message(trace) for trace in errors.errors[-1]['traces']]
			output.submessage('Skipping URL.\n')
