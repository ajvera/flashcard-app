from sqlalchemy import create_engine  
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base  
from sqlalchemy.orm import sessionmaker

db_string = "postgresql://avera:@+0Ku$@@localhost/flashapp"

db = create_engine(db_string)
base = declarative_base()

class Flashcard(base):
    __tablename__ = 'flashcards'

    flashcardID = Column(Integer, primary_key=True)
    term = Column(String)
    definition = Column(String)

Session = sessionmaker(db)  
session = Session()

base.metadata.create_all(db)