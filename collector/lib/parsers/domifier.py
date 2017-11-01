from htmldom import htmldom

def mutate(html):
	return htmldom.HtmlDom().createDom(html)
