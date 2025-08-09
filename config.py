import os
from pathlib import Path
from dotenv import load_dotenv

# Пути
BASE_DIR = Path(__file__).parent.parent

# Загрузка переменных
load_dotenv(BASE_DIR / '.env')

# Настройки
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(id) for id in os.getenv("ADMIN_IDS", "").split(",") if id]
DB_NAME = os.getenv("DB_NAME", "bot.db")  # Добавлено значение по умолчанию