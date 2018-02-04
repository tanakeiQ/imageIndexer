#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 
# Created by tanakeiQ<tanakei@suitehearts.co>
# 
import json
from bottle import run, route, template, static_file

@route('/')
def index():
	f = open('debug/output/_map.json', 'r')
	reader =  json.load(f)
	data = "{}".format(json.dumps(reader))
	f.close()
	return template('index',  {'data': data})

@route('/static/thumb/<filename>')
def server_static(filename):
    return static_file(filename, root='debug/output/thumb')


run(host='localhost', port=8080, debug=True)