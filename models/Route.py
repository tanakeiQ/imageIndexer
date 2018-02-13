#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by tanakeiQ<tanakei@suitehearts.co>
#
import sqlite3
from log import *


class Route:
    # TODO: 動的にcolumn_nameとselect_dir_namesを変更する
    column_name = ['階層 1', '階層 2', '階層 3', '階層 4',
                   '階層 5', '階層 6', '階層 7', '階層 8', '階層 9', '階層 10']
    select_dir_names = ['dir_1', 'dir_2', 'dir_3', 'dir_4',
                        'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9', 'dir_10']

    # def __init__(self):
    #     conn = sqlite3.connect('debug/main.db')
    #     conn.row_factory = sqlite3.Row
    #     cursor = conn.cursor()
    #     try:
    #         cursor.execute("""
    #             PRAGMA table_info(routes)
    #             """)
    #         result = cursor.fetchall()
    #     except sqlite3.Error as e:
    #         logger.info('Error: ', e.args[0])
    #         raise e
    #     conn.commit()
    #     cursor.close()
    #     conn.close()
    #     if not result is None:
    #         for key in result:
    #             self.column_name.append(key['name'])

    def get(self, id):
        conn = sqlite3.connect('debug/main.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT * FROM routes WHERE id = '%s' LIMIT 1
                """ % (id))
            result = cursor.fetchone()
        except sqlite3.Error as e:
            logger.info('Error: ', e.args[0])
            raise e
        conn.commit()
        cursor.close()
        conn.close()
        return result

    def getAll(self):
        conn = sqlite3.connect('debug/main.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            cursor.execute("""
            	SELECT id, %s, is_enabled FROM routes ORDER BY %s
            	""" % (','.join(self.select_dir_names), ','.join(self.select_dir_names)))
            result = cursor.fetchall()
        except sqlite3.Error as e:
            logger.info('Error: ', e.args[0])
            raise e
        conn.commit()
        cursor.close()
        conn.close()
        return self.setValue(result)

    def getDirectories(self, limit=10):
        conn = sqlite3.connect('debug/main.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        routes = {}
        try:
            cursor.execute("""
                SELECT r.id, r.path, r.description, i.thumbnail FROM routes AS r
                    INNER JOIN route_indexes AS ri
                    ON ri.route_id = r.id
                    INNER JOIN indexes AS i
                    ON i.id = ri.index_id
                """)
            result = cursor.fetchall()
            for route in result:
                if not route['id'] in routes:
                    routes[route['id']] = []
                if len(routes[route['id']]) < limit:
                    routes[route['id']].append(route)

        except sqlite3.Error as e:
            logger.info('Error: ', e.args[0])
            raise e
        conn.commit()
        cursor.close()
        conn.close()
        return routes

    def update(self, id, input):
        conn = sqlite3.connect('debug/main.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        keys = input.keys()
        values = list(
            map(lambda item: '%s = \'%s\'' % (item, input[item]), keys))
        try:
            cursor.execute("""
                UPDATE routes SET %s WHERE id = '%s'
                """ % (','.join(values), id))
        except sqlite3.Error as e:
            logger.info('Error: ', e.args[0])
            raise e
        conn.commit()
        cursor.close()
        conn.close()

    def setValue(self, result):
        return {
            "column": self.column_name,
            "column_key": self.select_dir_names,
            "result": result
        }
