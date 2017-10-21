from lib.processors.feed.processor import build as feed_processor_builder
from lib.processors.feed.source import build as feed_source_builder

def build_processor(config):
	if config['processor'] == 'feed':
		return feed_processor_builder()

	raise SourceErrorInvalidProcessor(config['processor'])

def build_source(config):
	if config['processor'] == 'feed':
		return feed_source_builder(config)

	raise SourceErrorInvalidProcessor(config['processor'])
	

class SourceError(RuntimeError): pass
class SourceErrorInvalidProcessor(SourceError): pass
