import logging
from flask import request, Response

logger = logging.getLogger(__name__)

def get_logs():
    try:
        with open('app.log', 'r') as log_file:
            logs = log_file.read()
        return Response(logs, mimetype='text/plain')
    except FileNotFoundError:
        return Response("Log file not found.", mimetype='text/plain', status=404)

def add():
    a = request.args.get('a')
    b = request.args.get('b')
    if a is None or b is None:
        return Response("Missing query parameters 'a' or 'b'", status=400)
    a = int(a)
    b = int(b)
    result = a + b
    logger.info(f"Adding {a} and {b} to get {result}")
    return f'The result of {a} + {b} is {result}'
