#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by tanakeiQ<tanakei@suitehearts.co>
#
import sqlite3
from log import *


class Index:

    def getByRouteId(self, id):
        conn = sqlite3.connect('debug/main.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        try:
            cursor.execute("""
				SELECT i.* FROM routes AS r
                    INNER JOIN route_indexes AS ri
                    ON ri.route_id = r.id
                    INNER JOIN indexes AS i
                    ON i.id = ri.index_id
                    WHERE r.id = '%s'
		    	""" % (id))
            result = cursor.fetchall()
        except sqlite3.Error as e:
            logger.info('Error: ', e.args[0])
            raise e
        conn.commit()
        cursor.close()
        conn.close()
        return result
