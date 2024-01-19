from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database

from config import config

engine = create_engine(config['SQLALCHEMY_DATABASE_URI'])

if not database_exists(engine.url):
    create_database(engine.url)

db_session = scoped_session(
    sessionmaker(autocommit=False, autoflush=False, bind=engine)
)
Base = declarative_base()
Base.query = db_session.query_property()
