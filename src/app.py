from flask import Flask, Blueprint
from src.db import db, migrate
import os
from src.api import init_api

POSTGRES_DB = os.environ.get('POSTGRES_DB')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')


def create_app(config_file=None, settings_override=None):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@db:5432/{POSTGRES_DB}'

    db.init_app(app)
    migrate.init_app(app, db)

    init_api(app)

    return app


if __name__ == "__main__":
    create_app()
