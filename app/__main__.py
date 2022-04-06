"""Main module"""

import logging

import app.routes

logging.basicConfig(
    filename='flask_todo.log',
    level=logging.DEBUG,
    filemode='w')

app.routes.run()
