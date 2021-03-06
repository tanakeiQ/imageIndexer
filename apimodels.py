import sqlite3
from log import *
import uuid

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
                id TEXT NOT NULL PRIMARY KEY,
                uid TEXT NOT NULL,
                name TEXT NOT NULL,
                ext TEXT NULL,
                path TEXT NOT NULL,
                thumbnail TEXT NOT NULL,
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


def initRoutes(hierarchy=1):
    conn = sqlite3.connect('debug/main.db')
    cursor = conn.cursor()
    try:
        dirs = ""
        for i in range(hierarchy):
            dirs += "dir_%s TEXT NULL," % (str(i + 1))
        conn.execute("""
            CREATE TABLE IF NOT EXISTS routes (
                id TEXT NOT NULL PRIMARY KEY,
                path TEXT NOT NULL,
                %s
                description TEXT NULL,
                is_enabled TINYINT(1) NOT NULL DEFAULT 0,
                created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                deleted_at TIMESTAMP NULL
            )
            """ % (dirs))
    except sqlite3.Error as e:
        logger.info('Error: ', e.args[0])
        raise e
    conn.commit()
    cursor.close()
    conn.close()


def initRouteIndexes():
    conn = sqlite3.connect('debug/main.db')
    cursor = conn.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS route_indexes (
                route_id TEXT NOT NULL,
                index_id TEXT NULL,
                created_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP
            )
            """)
        conn.execute("""
            CREATE INDEX IF NOT EXISTS idx__route_id__index_id ON route_indexes(route_id, index_id)
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
        cursor.execute('SELECT 1 FROM indexes WHERE uid = "%s"' %
                       (data['uid']))
        result = cursor.fetchone()
        if result is None:
            data['id'] = uuid.uuid4()
            cursor.execute("""
                INSERT INTO indexes
                    (id, uid, name, ext, path, thumbnail, size, width, height)
                VALUES
                    ("{id}", "{uid}", "{name}", "{ext}", "{path}",
                     "{thumbnail}", "{size}", "{width}", "{height}")
                """.format(**data))
        else:
            logger.info('%s is already exists' % (data['uid']))
    except sqlite3.Error as e:
        logger.warning('Error: ', e.args[0])
        logger.info('😂  DEBUG:: %s' % (data['path']))
    conn.commit()
    cursor.close()
    conn.close()


def createRoute(rootpath, fullpath):
    conn = sqlite3.connect('debug/main.db')
    cursor = conn.cursor()

    data = fullpath.replace(rootpath, '').split('/')
    dirs = {
        'id': str(uuid.uuid4()),
        'path': fullpath.replace(rootpath, '')
    }
    for i in range(len(data)):
        dirs.update({'dir_%d' % (i + 1): str(data[i])})
    keys = dirs.keys()
    dir_query = list(map(lambda item: '\"{%s}\"' % (item), keys))
    try:
        cursor.execute('SELECT 1 FROM routes WHERE id = "%s"' % (dirs['id']))
        result = cursor.fetchone()
        if result is None:
            query = """
                INSERT INTO routes
                    (%s)
                VALUES
                    (%s)
                """ % (','.join(keys), ','.join(dir_query))
            conn.execute(query.format(**dirs))
        else:
            logger.info('[routes]: %s is already exists' % (dirs['id']))
    except sqlite3.Error as e:
        logger.warning('Error: ', e.args[0])
        logger.info('😂  DEBUG:: %s' % (fullpath))
    conn.commit()
    cursor.close()
    conn.close()
