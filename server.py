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
    print(request.forms.decode().getall('disabled'))
    print(request.forms.decode().getall('actived[]'))
    redirect("/routes")


@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root=app.config['resource.static_path'])


run(host=app.config['server.host'],
    port=app.config['server.port'],
    debug=app.config['server.is_debug'],
    reloader=app.config['server.is_auto_reload'])
