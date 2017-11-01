import sqlite3

from lib.util import config

def initialize():
	conn = sqlite3.connect(config.DB_PATH)
	cursor = conn.cursor()

	if entries_table_missing(cursor):
		create_entries_table(cursor)

	conn.close()

def entries_table_missing(cursor):
	cursor.execute('''
		SELECT name
		FROM sqlite_master 
		WHERE 
			type="table" AND 
			name="entries"''')

	return cursor.fetchone() is None

def create_entries_table(cursor):
	cursor.execute('''
		CREATE TABLE "entries" 
		( 
			`id` TEXT NOT NULL, 
			`url` TEXT NOT NULL, 
			`author` TEXT, 
			`summary` TEXT, 
			`content` TEXT NOT NULL, 
			`published` NUMERIC, 
			`title` TEXT, 
			`tags` TEXT, 
			`image` TEXT, 
			`site` TEXT, 
			PRIMARY KEY(`id`)
		)''')
