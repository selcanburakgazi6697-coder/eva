import os
import requests
import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

TOKEN = os.environ.get("TOKEN")
GAME_URL = "https://eva-casino.pages.dev"
ADMIN_IDS = [8101681923]

bot = telebot.TeleBot(TOKEN)
ANIMATION_FILE_ID = None

def get_markup():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(
        "✦ Открыть Eva Casino ✦",
        web_app=WebAppInfo(url=GAME_URL)
    ))
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    global ANIMATION_FILE_ID
    caption = "🎰 Eva Casino — твоё место удачи!\n\nБонусы, кешбэк до 20% и тысячи игр ждут тебя 👇"
    markup = get_markup()

    if ANIMATION_FILE_ID:
        bot.send_animation(message.chat.id, ANIMATION_FILE_ID, caption=caption, reply_markup=markup)
    else:
        video_path = os.path.join(os.path.dirname(__file__), "eva.mp4")
        if os.path.exists(video_path):
            with open(video_path, "rb") as f:
                sent = bot.send_animation(message.chat.id, f, caption=caption, reply_markup=markup)
                ANIMATION_FILE_ID = sent.animation.file_id
        else:
            bot.send_message(message.chat.id, caption, reply_markup=markup)

print("Eva bot started...")
bot.infinity_polling()
