from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base
from config import DB_NAME
from loguru import logger
import os

# Путь к базе данных
DB_PATH = f"sqlite:///{os.path.abspath(DB_NAME)}"

Base = declarative_base()

class Database:
    def __init__(self):
        self.engine = create_engine(DB_PATH)
        self.Session = scoped_session(sessionmaker(bind=self.engine))
        
        try:
            Base.metadata.create_all(self.engine)
            logger.success("Database tables created")
        except Exception as e:
            logger.error(f"Database error: {e}")

    def get_session(self):
        return self.Session()

    def close_session(self):
        self.Session.remove()

# Глобальный экземпляр БД
db = Database()

def init_db():
    """Инициализация базы данных"""
    try:
        Base.metadata.create_all(db.engine)
        logger.info("Database initialized")
    except Exception as e:
        logger.error(f"Init DB error: {e}")
        raise