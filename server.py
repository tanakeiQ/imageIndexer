#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Created by tanakeiQ<tanakei@suitehearts.co>
#
import json
import bottle
from models import Route
from bottle import run, get, post, request, redirect, template, static_file

app = bottle.default_app()
app.config.load_config([
    'config/resource.ini',
    'config/server.ini'
])

print(app.config)


@get('/routes')
def index():
    _route = Route.Route()
    routes = _route.getAll()
    return template('index', {'routes': routes})


@post('/routes')
def index():
    actived = request.forms.decode().getall('actived[]')
    disabled = request.forms.decode().getall('disabled[]')

    _route = Route.Route()

    if len(actived) > 0:
        for id in actived:
            routes = _route.update(id, {'is_enabled': 1})

    if len(disabled) > 0:
        for id in disabled:
            routes = _route.update(id, {'is_enabled': 0})

    redirect("/routes")


@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=app.config['resource.static_path'])


run(host=app.config['server.host'],
    port=app.config['server.port'],
    debug=app.config['server.is_debug'],
    reloader=app.config['server.is_auto_reload'])
