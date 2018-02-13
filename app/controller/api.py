from bottle import request, response, abort
from bottle import get, post
import os
import json
import sys
from log import *
from models import Route

response.headers['Content-Type'] = 'application/json'


@post('/api/routes/<id>')
def routes(id):
    try:
        description = request.params.decode().get('description')
        if not description:
            abort(402)
        route = Route.Route()
        route.update(id, {"description": description})
        return json.dumps({"result": "success"})
    except:
        logger.info(sys.exc_info())
        abort(500)
