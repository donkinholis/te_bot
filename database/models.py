from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from .db import Base

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=True)
    first_name = Column(String(50))
    last_name = Column(String(50), nullable=True)
    is_admin = Column(Boolean, default=False)
    join_date = Column(DateTime, default=datetime.now)

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True)
    type = Column(String(10))  # 'photo', 'music', 'quote'
    file_id = Column(String(255))
    caption = Column(String(500), nullable=True)
    created_at = Column(DateTime, default=datetime.now)