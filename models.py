import sqlite3
from log import *

conn = None

def close():
	if not conn is None:
		conn.close()
		logger.info('🌀  closed')

# Indexes indexes
# uid
# name
# ext
# path
# filename
# size
# width
# height


def initIndex():
	conn = sqlite3.connect('debug/main.db')
	cursor = conn.cursor()
	try:
		cursor.execute("""
			CREATE TABLE IF NOT EXISTS indexes (
				uid TEXT NOT NULL PRIMARY KEY, 
				name TEXT NOT NULL, 
				ext TEXT NULL, 
				path TEXT NOT NULL,
				filename TEXT NOT NULL,
				size INTEGER NOT NULL DEFAULT 0,
				width INTEGER NULL DEFAULT 0,
				height INTEGER NULL DEFAULT 0,
				created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
				updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
				deleted_at TIMESTAMP NULL
			)
			""")
	except sqlite3.Error as e:
		logger.info('Error: ', e.args[0])
		raise e
	conn.commit()
	cursor.close()
	conn.close()


def createIndex(data):
	conn = sqlite3.connect('debug/main.db')
	cursor = conn.cursor()
	try:
		cursor.execute("SELECT 1 FROM indexes WHERE uid = '%s'" % (data['uid']))
		result=cursor.fetchone()
		if result is None:
			cursor.execute("""
				INSERT INTO indexes 
					(uid, name, ext, path, filename, size, width, height) 
				VALUES
					('{uid}', '{name}', '{ext}', '{path}', '{filename}', '{size}', '{width}', '{height}')
				""".format(**data))
		else:
			logger.info('%s is already exists' % (data['uid']))
	except sqlite3.Error as e:
		logger.warning('Error: ', e.args[0])
		raise e
	conn.commit()
	cursor.close()
	conn.close()
	return True
