#!/usr/bin/env python

from flask_script import Manager
from flask_migrate import MigrateCommand

from app import create_app


manager = Manager(create_app)
manager.add_option('-c', '--config', dest='config_file', required=False)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()