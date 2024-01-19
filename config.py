import os

from inspira.config import Config

config = Config()

config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
