import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import Base

class picdocument(Base):
    __tablename__ = 'picdocument'
    pdocid = Column(Integer, primary_key=True)
    pcateid = Column(Integer)
    title = Column(String(80), unique=True)

    docno = Column(String(120))
    docname = Column(String(120))
    docpath = Column(String(120))
    tags = Column(String(120))

    def __init__(self):
        pass

    def __repr__(self):
        return '<title %r>' % (self.title)
