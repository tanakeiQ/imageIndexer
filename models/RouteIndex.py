#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by tanakeiQ<tanakei@suitehearts.co>
#
import sqlite3
from log import *
from models import Route


class RouteIndex:
    select_dir_names = ['dir_1', 'dir_2', 'dir_3', 'dir_4',
                        'dir_5', 'dir_6', 'dir_7', 'dir_8', 'dir_9', 'dir_10']

    def associate(self, id):
        conn = sqlite3.connect('debug/main.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            cursor.execute("""
                SELECT %s FROM routes WHERE ID = "%s"
                """ % (','.join(self.select_dir_names), id))
            route = cursor.fetchone()
            if not route == None:
                path = '/'.join(filter(lambda item: item is not None and len(item) > 0, route))
                print(path)
                cursor.execute("""
                   SELECT id FROM indexes WHERE path LIKE "%s"
                   """ % (path + '%'))
                indexes = cursor.fetchall()
                for index in indexes:
                    conn.execute("""
                        INSERT INTO route_indexes
                            (route_id, index_id)
                        VALUES
                            ("%s", "%s")
                        """ % (id, index['id']))
        except sqlite3.Error as e:
            logger.info('Error: ', e.args[0])
            raise e
        conn.commit()
        cursor.close()
        conn.close()

    def disassociate(self, id):
        conn = sqlite3.connect('debug/main.db')
        cursor = conn.cursor()
        try:
            cursor.execute("""
                DELETE FROM route_indexes WHERE route_id = "%s"
                """ % (id))
        except sqlite3.Error as e:
            logger.info('Error: ', e.args[0])
            raise e
        conn.commit()
        cursor.close()
        conn.close()
