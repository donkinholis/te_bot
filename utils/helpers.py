import os
import random
import string
from datetime import datetime
from typing import Union, Optional
from loguru import logger
from config import BASE_DIR

def generate_random_string(length: int = 8) -> str:
    """Генерує випадковий рядок для тимчасових файлів"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def clean_temp_files(max_age_hours: int = 1):
    """Очищає тимчасові файли старші за вказаний час"""
    temp_dir = os.path.join(BASE_DIR, 'temp')
    if not os.path.exists(temp_dir):
        return
        
    now = datetime.now()
    for filename in os.listdir(temp_dir):
        file_path = os.path.join(temp_dir, filename)
        try:
            file_time = datetime.fromtimestamp(os.path.getmtime(file_path))
            if (now - file_time).total_seconds() > max_age_hours * 3600:
                os.remove(file_path)
                logger.info(f"Deleted temp file: {filename}")
        except Exception as e:
            logger.error(f"Error deleting temp file {filename}: {e}")

def validate_file_type(filename: str, allowed_types: list) -> bool:
    """Перевіряє тип файлу"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in allowed_types

def get_file_size_mb(file_path: str) -> float:
    """Повертає розмір файлу в мегабайтах"""
    return os.path.getsize(file_path) / (1024 * 1024)

def create_directory_if_not_exists(path: str):
    """Створює директорію, якщо вона не існує"""
    if not os.path.exists(path):
        os.makedirs(path)
        logger.info(f"Created directory: {path}")

def split_text(text: str, max_length: int = 4000) -> list[str]:
    """Розбиває довгий текст на частини для Telegram"""
    return [text[i:i+max_length] for i in range(0, len(text), max_length)]

def format_user_info(user) -> str:
    """Форматує інформацію про користувача для логування"""
    return (f"ID: {user.id} | "
            f"Username: @{user.username} | "
            f"Name: {user.first_name} {user.last_name or ''}")

def is_admin(user_id: int) -> bool:
    """Перевіряє, чи є користувач адміном"""
    from database.db import db
    session = db.get_session()
    try:
        from models import User
        user = session.query(User).filter(User.id == user_id).first()
        return user.is_admin if user else False
    finally:
        db.close_session()

def convert_seconds(seconds: int) -> str:
    """Конвертує секунди у читабельний формат (HH:MM:SS)"""
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"