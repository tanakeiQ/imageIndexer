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
    f = open(app.config['resource.map_path'], 'r')
    reader = json.load(f)
    data = "{}".format(json.dumps(reader))
    f.close()
    return template('index',  {'data': data})


@route('/static/thumb/<filename>')
def server_static(filename):
    return static_file(filename, root=app.config['resource.static_path'])


run(host=app.config['server.host'], port=app.config[
    'server.port'], debug=app.config['server.is_debug'])
