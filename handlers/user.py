from telegram import Update
from telegram.ext import CallbackContext
from utils.logger import logger
from utils.keyboards import main_menu_keyboard
from database.db import db
from database.models import User

async def start(update: Update, context: CallbackContext):
    try:
        user = update.effective_user
        logger.info(f"New user: {user.id}")
        
        session = db.get_session()
        if not session.query(User).filter(User.id == user.id).first():
            new_user = User(
                id=user.id,
                username=user.username,
                first_name=user.first_name
            )
            session.add(new_user)
            session.commit()
        
        await update.message.reply_text(
            "Оберіть дію:",
            reply_markup=main_menu_keyboard()
        )
    except Exception as e:
        logger.error(f"Start error: {e}")
        await update.message.reply_text("❌ Помилка")
    finally:
        db.close_session()

async def handle_main_menu_buttons(update: Update, context: CallbackContext):
    try:
        text = update.message.text
        logger.info(f"Pressed button: {text}")
        
        if text == "📸 Випадкове фото":
            from .posts import send_random_photo
            await send_random_photo(update, context)
        elif text == "🎵 Випадкова музика":
            from .posts import send_random_music
            await send_random_music(update, context)
        elif text == "💬 Випадкова цитата":
            from .posts import send_random_quote
            await send_random_quote(update, context)
        else:
            await update.message.reply_text("❌ Невідома команда")
    except Exception as e:
        logger.error(f"Button error: {e}")
        await update.message.reply_text("❌ Помилка обробки")