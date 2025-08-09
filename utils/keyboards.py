from telegram import (
    ReplyKeyboardMarkup,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

def main_menu_keyboard():
    """Головне меню"""
    buttons = [
        ["📸 Випадкове фото", "🎵 Випадкова музика"],
        ["💬 Випадкова цитата", "🔍 Пошук YouTube"]
    ]
    return ReplyKeyboardMarkup(buttons, resize_keyboard=True)

def admin_keyboard():
    """Клавіатура адміна"""
    buttons = [
        [InlineKeyboardButton("📊 Статистика", callback_data="stats")],
        [InlineKeyboardButton("📢 Розсилка", callback_data="broadcast")]
    ]
    return InlineKeyboardMarkup(buttons)

def youtube_options(video_url):
    """Варіанти для YouTube"""
    buttons = [
        [InlineKeyboardButton("⬇️ MP3", callback_data=f"dl_audio_{video_url}")],
        [InlineKeyboardButton("⬇️ MP4", callback_data=f"dl_video_{video_url}")]
    ]
    return InlineKeyboardMarkup(buttons)