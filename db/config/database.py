from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


DATABASE_URL = 'postgresql://postgres:221094@localhost:5432/db_concierge'


engine = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(autocommit= False, autoflush=False, bind=engine)

Base = declarative_base()

def create_bd():
    Base.metadata.create_all(bind=engine)

def get_db():
    db =SessionLocal()
    try:
        yield db
    finally:
        db.close()