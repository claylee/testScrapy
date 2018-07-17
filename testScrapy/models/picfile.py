import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from database import Base

class picfile(Base):
    __tablename__ = 'picfile'
    pid = Column(Integer, primary_key=True)
    cateid = Column(Integer)
    did = Column(Integer)
    fileno = Column(Integer)

    pictitle = Column(String(120))
    picurl = Column(String(120))
    md5code = Column(String(120))
    tags = Column(String(120))

    def __init__(self):
        pass

    def __repr__(self):
        return '<title %r>' % (self.title)
