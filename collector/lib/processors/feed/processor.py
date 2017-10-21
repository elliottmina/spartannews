import requests
import feedparser
from email.utils import parsedate_tz
from email.utils import mktime_tz
from pprint import pprint

from lib.processors.feed.filters import filters
from lib import persistor

instance = None

def build():
	if not instance:
		instantiate()
	return instance

def instantiate():
	global instance
	instance = Processor(filters.get(), persistor)

class Processor:
	def __init__(self, filters, persistor):
		self.filters = filters
		self.persistor = persistor

	def process(self, source):
		feed = self.get_feed(source)
		[self.process_entry(source, entry) for entry in feed['entries']]

	def get_feed(self, source):
		feed = feedparser.parse(source.url)
		return self.mutate(source.rss_mutators, feed)

	def process_entry(self, source, entry):
		print('> Processing entry "{}".'.format(entry.id))

		if self.filters.is_blocked(entry):
			return

		self.persistor.upsert({
			'id': entry.id,
			'link': entry.link,
			'author': entry.author,
			'summary': entry.summary,
			'content': self.build_html(source, entry),
			'published': self.build_timestamp(entry),
			'title': entry.title,
		})

	def build_html(self, source, entry):
		html = self.get_html(entry)
		return self.mutate(source.html_mutators, html)

	def build_timestamp(self, entry):
		return mktime_tz(parsedate_tz(entry.published))

	def get_html(self, entry):
		return requests.get(entry.link).text

	def mutate(self, mutators, mutatee):
		for mutator in mutators:
			mutatee = mutator.mutate(mutatee)
		return mutatee
