from bs4 import BeautifulSoup

from lib.meta_extractor import parsely
from lib.meta_extractor import open_graph
from lib.meta_extractor import ld_json
from lib.meta_extractor import misc_tags
from lib.meta_extractor import twitter

from pprint import pprint

def extract(html):
	soup = BeautifulSoup(html, 'html.parser')
	payload = {}
	
	parsely.build(soup, payload)
	open_graph.build(soup, payload)
	ld_json.build(soup, payload)
	misc_tags.build(soup, payload)
	twitter.build(soup, payload)

	return payload
