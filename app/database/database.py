from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

HOST = os.getenv('DB_HOST', "")
DB = os.getenv('DB_NAME', "")
PASSWORD = os.getenv('DB_PASSWORD', "")
USER = os.getenv('DB_USER', "")

SQLALCHEMY_DATABASE_URL = "postgresql://{}:{}@{}/{}".format(USER, PASSWORD, HOST, DB)

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()