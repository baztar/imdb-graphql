from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from os import environ as env

engine = create_engine(env.get('ALCHEMY_URL', 'postgresql://taras@localhost/taras'), echo='SQLALCHEMY_ECHO' in env)

session = scoped_session(sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
))

Base = declarative_base()
Base.query = session.query_property()


def init_db():
    from .models import Title, Movie, Series, Episode, EpisodeInfo, Rating, Name
    Base.metadata.reflect(engine)
