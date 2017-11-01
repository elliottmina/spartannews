import requests

from lib.parsers import soupify

def mutate(soup):
	url = get_amp_url(soup)
	if not url:
		return soup

	html = requests.get(url).text
	return soupify.mutate(html)

def get_amp_url(soup):
	amp_link = soup.find('link', rel='amphtml')
	if amp_link: 
		return amp_link.get('href')

