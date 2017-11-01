from lib.processors.feed.processor import Processor as FeedProcessor
from lib.processors.index.processor import Processor as IndexProcessor
from lib.processors.feed.filters import filters as feed_filters
from lib.processors.feed.source import build as feed_source_builder
from lib.processors.index.source import build as index_source_builder

feed_processor = FeedProcessor(feed_filters.get())
index_processor = IndexProcessor(None)

def build_processor(config):
	if config['processor'] == 'feed':
		return feed_processor

	if config['processor'] == 'index':
		return index_processor

	raise SourceErrorInvalidProcessor(config['processor'])

def build_source(config):
	if config['processor'] == 'feed':
		return feed_source_builder(config)

	if config['processor'] == 'index':
		return index_source_builder(config)

	raise SourceErrorInvalidProcessor(config['processor'])

class SourceError(RuntimeError): pass
class SourceErrorInvalidProcessor(SourceError): pass
