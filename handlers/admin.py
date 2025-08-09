from telegram import Update
from telegram.ext import CallbackContext
from utils.logger import logger
from utils.keyboards import admin_keyboard, main_menu_keyboard
from config import ADMIN_IDS

async def admin_panel(update: Update, context: CallbackContext):
    """Обробник адмін-панелі"""
    try:
        user = update.effective_user
        
        if user.id not in ADMIN_IDS:
            logger.warning(f"Спроба доступу: {user.id}")
            await update.message.reply_text(
                "⛔ Недостатньо прав!",
                reply_markup=main_menu_keyboard()
            )
            return

        await update.message.reply_text(
            "👨‍💻 <b>Адмін-панель</b>:",
            parse_mode="HTML",
            reply_markup=admin_keyboard()
        )
    except Exception as e:
        logger.error(f"Помилка адмінки: {e}")
        await update.message.reply_text("❌ Помилка панелі")