import requests
import feedparser
import dateutil.parser
import time
from pprint import pprint

from lib.util.mutate import mutate

def get_feed(source):
	feed = feedparser.parse(source.url)
	return mutate(source.rss_mutators, feed)

def build_html(source, entry):
	html = get_html(entry)
	return mutate(source.html_mutators, html)

def build_timestamp(entry):
	date = dateutil.parser.parse(entry.published)
	return time.mktime(date.timetuple())

def get_html(entry):
	return requests.get(entry.link).text

class Processor:
	def __init__(self, filters):
		self.filters = filters

	def process(self, upserter, source):
		feed = get_feed(source)
		[self.process_entry(upserter, source, entry) for entry in feed['entries']]

	def process_entry(self, upserter, source, entry):
		print('> Processing entry "{}".'.format(entry.id))
		pprint(entry)

		if self.filters.is_blocked(entry):
			return

		upserter.upsert({
			'id': entry.id,
			'url': entry.link,
			'author': entry.author,
			'summary': entry.summary,
			'content': build_html(source, entry),
			'published': build_timestamp(entry),
			'title': entry.title,
		})

