from bs4 import BeautifulSoup

def mutate(html):
	return BeautifulSoup(html, 'html.parser')
