from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import CallbackContext
from utils.logger import logger
from utils.keyboards import youtube_options
import yt_dlp as youtube_dl

async def search_youtube(update: Update, context: CallbackContext):
    """Пошук на YouTube"""
    try:
        query = update.message.text
        # Тимчасовий приклад URL (у реальному боті тут буде пошук)
        video_url = "https://youtu.be/dQw4w9WgXcQ"  
        
        await update.message.reply_text(
            f"🔍 Результати для: <b>{query}</b>",
            parse_mode="HTML",
            reply_markup=youtube_options(video_url)
        )
    except Exception as e:
        logger.error(f"Помилка YouTube: {e}")
        await update.message.reply_text("❌ Помилка пошуку")