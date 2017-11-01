import sqlite3

from lib.util import config

known_cols = ['id', 'url', 'author', 'summary', 'content', 'published', 
	'title', 'site', 'image', 'tags',]

template = 'INSERT OR REPLACE INTO entries ({}) VALUES ({})'

def build_sql(entry):
	cols = [col for col in known_cols if col in entry]
	col_sql = ', '.join(cols)
	placeholders = ('?, '*len(cols))[0:-2]
	return template.format(col_sql, placeholders)

def build_params(entry):
	return [col for col in known_cols if col in entry]

class EntryUpserter():
	
	def __enter__(self):
		self.conn = sqlite3.connect(config.DB_PATH)
		self.cursor = self.conn.cursor()
		return self

	def __exit__(self, type, value, traceback):
		self.conn.close()

	def upsert(self, entry):
		sql = build_sql(entry)
		params = build_params(entry)
		self.cursor.execute(sql, params)
		self.conn.commit()
