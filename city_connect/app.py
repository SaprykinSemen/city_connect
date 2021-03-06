import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from city_connect.config import runtime_config


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


# dev, prod, test
APP_STATUS = 'dev'


app = Flask(__name__)
app.config.from_object(runtime_config(APP_STATUS))

db = SQLAlchemy(app)

with app.app_context():
    db.create_all()


# application routes
from city_connect.views.index import Index

index_view = Index.as_view('index')
app.add_url_rule('/', view_func=index_view, methods=['GET'])


# error handlers
from city_connect.views.error_handlers import (
    page_not_found,
    forbidden,
    gone,
    internal_server_error,
)

app.register_error_handler(404, page_not_found)
app.register_error_handler(403, forbidden)
app.register_error_handler(410, gone)
app.register_error_handler(500, internal_server_error)
