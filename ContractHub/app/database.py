import os 

from sqlalchemy import create_engine 
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

db_url1 = os.getenv("DATABASE_URL")

if not db_url1: 
        raise ValueError("DATABASE_URL is not set in the environment variables.")

DATABASE_URL = db_url1 

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=engine)    

Base = declarative_base()