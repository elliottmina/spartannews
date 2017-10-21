import sqlite3

from lib import config

upsert_template = '''INSERT OR REPLACE INTO entries 
	(`id`, `link`, `author`, `summary`, `content`, `published`, `title`)
	VALUES (?, ?, ?, ?, ?, ?, ?)'''

def upsert(entry):
	execute(upsert_template, [
		entry['id'],
		entry['link'],
		entry['author'],
		entry['summary'],
		entry['content'],
		entry['published'],
		entry['title'],])

def execute(sql, values):
	conn = sqlite3.connect(config.BASE_DIR + '/db')
	cursor = conn.cursor()
	cursor.execute(sql, values)
	conn.commit()
	conn.close()
