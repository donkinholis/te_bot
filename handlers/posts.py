from telegram import Update
from telegram.ext import CallbackContext
from utils.logger import logger
from config import BASE_DIR
import os
import random

async def send_random_photo(update: Update, context: CallbackContext):
    try:
        photos = os.listdir(os.path.join(BASE_DIR, 'assets', 'photos'))
        photos = [f for f in photos if f.endswith(('.jpg', '.png'))]
        
        if photos:
            photo_path = os.path.join(BASE_DIR, 'assets', 'photos', random.choice(photos))
            with open(photo_path, 'rb') as photo:
                await update.message.reply_photo(photo, caption="📸 Ваше фото")
        else:
            await update.message.reply_text("Фото не знайдено")
    except Exception as e:
        logger.error(f"Photo error: {e}")
        await update.message.reply_text("❌ Помилка фото")

async def send_random_music(update: Update, context: CallbackContext):
    try:
        music = os.listdir(os.path.join(BASE_DIR, 'assets', 'music'))
        music = [f for f in music if f.endswith('.mp3')]
        
        if music:
            music_path = os.path.join(BASE_DIR, 'assets', 'music', random.choice(music))
            with open(music_path, 'rb') as audio:
                await update.message.reply_audio(audio)
        else:
            await update.message.reply_text("Музика не знайдена")
    except Exception as e:
        logger.error(f"Music error: {e}")
        await update.message.reply_text("❌ Помилка музики")

async def send_random_quote(update: Update, context: CallbackContext):
    try:
        quotes = os.listdir(os.path.join(BASE_DIR, 'assets', 'quotes'))
        quotes = [f for f in quotes if f.endswith('.txt')]
        
        if quotes:
            quote_path = os.path.join(BASE_DIR, 'assets', 'quotes', random.choice(quotes))
            with open(quote_path, 'r', encoding='utf-8') as f:
                await update.message.reply_text(f"📜 Цитата:\n\n{f.read()}")
        else:
            await update.message.reply_text("Цитати не знайдено")
    except Exception as e:
        logger.error(f"Quote error: {e}")
        await update.message.reply_text("❌ Помилка цитати")