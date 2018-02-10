#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by tanakeiQ<tanakei@suitehearts.co>
#
import json
import bottle
from bottle import run, route, template, static_file

app = bottle.default_app()
app.config.load_config([
    'config/resource.ini',
    'config/server.ini'
])

print(app.config)


@route('/')
def index():
    return template('index',  {'data': None})


@route('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=app.config['resource.static_path'])


run(host=app.config['server.host'], 
	port=app.config['server.port'],
	debug=app.config['server.is_debug'],
	reloader=app.config['server.is_auto_reload'])
