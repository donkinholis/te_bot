import sys
from pathlib import Path
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    CallbackContext
)
from handlers import start, help_command, admin_panel, search_youtube, handle_main_menu_buttons
from database.db import init_db
from loguru import logger
import os
from dotenv import load_dotenv
from telegram.error import TelegramError

# Налаштування шляхів
sys.path.append(str(Path(__file__).parent))

# Завантаження змінних середовища
load_dotenv()

# Конфігурація
TOKEN = os.getenv("BOT_TOKEN")
ADMIN_IDS = [int(id) for id in os.getenv("ADMIN_IDS", "").split(",") if id]

async def post_init(app):
    """Налаштування команд бота"""
    await app.bot.set_my_commands([
        ("start", "Головне меню"),
        ("help", "Довідка"),
        ("admin", "Адмін-панель"),
    ])

async def error_handler(update: object, context: CallbackContext):
    """Обробник помилок"""
    logger.error(f"Помилка: {context.error}")
    return True

def main():
    # Ініціалізація БД
    init_db()
    
    try:
        # Створення додатку
        app = Application.builder() \
            .token(TOKEN) \
            .post_init(post_init) \
            .build()
        
        # Обробники команд
        app.add_handler(CommandHandler("start", start))
        app.add_handler(CommandHandler("help", help_command))
        
        # Обробник адмін-панелі
        if ADMIN_IDS:
            app.add_handler(CommandHandler(
                "admin", 
                admin_panel, 
                filters=filters.User(ADMIN_IDS)
            )
        )
        # Обробник текстових повідомлень
        app.add_handler(MessageHandler(
            filters.TEXT & ~filters.COMMAND, 
            search_youtube
        ))
        
        # Обробник кнопок меню
        app.add_handler(MessageHandler(
            filters.TEXT & (
                filters.Regex("^📸 Випадкове фото$") |
                filters.Regex("^🎵 Випадкова музика$") |
                filters.Regex("^💬 Випадкова цитата$")
            ),
            handle_main_menu_buttons
        ))
        
        # Обробник помилок
        app.add_error_handler(error_handler)
        
        logger.info("🤖 Бот запущений!")
        app.run_polling()
        
    except Exception as e:
        logger.error(f"Помилка запуску: {e}")
        raise
# ... інші імпорти ...

def main():
    init_db()
    
    try:
        app = Application.builder().token(TOKEN).build()
        
        # Обробники команд
        app.add_handler(CommandHandler("start", start))
        
        # Обробник кнопок головного меню
        app.add_handler(MessageHandler(
            filters.TEXT & (
                filters.Regex("^📸 Випадкове фото$") |
                filters.Regex("^🎵 Випадкова музика$") |
                filters.Regex("^💬 Випадкова цитата$")
            ),
            handle_main_menu_buttons
        ))
        
        logger.info("Бот запущений!")
        app.run_polling()
    except Exception as e:
        logger.error(f"Помилка: {e}")
if __name__ == "__main__":
    main()