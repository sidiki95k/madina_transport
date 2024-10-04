

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session


SQLALCHEMY_DATABASE_URL = "postgresql://postgres:postgres@db/madina_transport_db"


engine = create_engine(SQLALCHEMY_DATABASE_URL)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base = declarative_base()

def get_db() -> Session:
    """
    Dependency that provides a database session for the FastAPI routes.
    Yields a session and closes it after use.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
