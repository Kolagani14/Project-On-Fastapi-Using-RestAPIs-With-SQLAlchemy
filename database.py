from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
db_url="postgresql://postgres:269@localhost:5432/db"
engine=create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Provide a lowercase `session` name so existing imports keep working
session = SessionLocal