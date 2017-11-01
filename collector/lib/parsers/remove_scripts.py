def mutate(soup):
	[script.extract() for script in soup('script')]
	return soup
