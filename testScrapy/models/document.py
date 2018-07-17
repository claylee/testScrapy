import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import Base

class picdocument(Base):
    __tablename__ = 'picdocument'
    did = Column(Integer, primary_key=True)
    pictitle = Column(String(80), unique=True)
    cateid = Column(Integer)

    docno = Column(String(120))
    docname = Column(String(120))
    docurl = Column(String(120))
    tags = Column(String(120))

    def __init__(self):
        pass

    def __repr__(self):
        return '<title %r>' % (self.title)
