from loguru import logger
import os
from datetime import datetime
from pathlib import Path

# Шлях до папки з логами
LOG_DIR = Path(__file__).parent.parent / "logs"
LOG_DIR.mkdir(exist_ok=True)

# Налаштування логера
logger.add(
    LOG_DIR / f"bot_{datetime.now().strftime('%Y-%m-%d')}.log",
    rotation="10 MB",
    retention="7 days",
    level="INFO",
    format="{time:YYYY-MM-DD HH:mm:ss} | {level} | {message}"
)

# Додаткові функції (якщо потрібні)
def log_error(error: Exception):
    """Логує помилки з деталями"""
    logger.error(f"Error: {str(error)}")