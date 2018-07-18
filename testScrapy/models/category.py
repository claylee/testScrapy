import os
import sqlite3
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
#from database import Base
from database import Base
import scrapy

class piccategory(Base):
    __tablename__ = 'piccategory'
    pcateid = Column(Integer, primary_key=True)

    title = Column(String(80), unique=True)
    text = Column(String(120))
    categoryno = Column(String(120))
    categoryname = Column(String(120))
    categoryurl = Column(String(120))
    tags = Column(String(120))

    def __init__(self):
        print("-----base------")
        pass

    def __repr__(self):
        return '<piccategory %r>' % (self.title)

    def testBase(self):
        print("-----base------")
