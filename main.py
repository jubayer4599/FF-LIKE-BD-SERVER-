import telebot
from telebot import types
import os
from flask import Flask
from threading import Thread

# Flask App তৈরি (Render-এর জন্য)
app = Flask('')

@app.route('/')
def home():
    return "Bot is alive!"

def run_flask():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run_flask)
    t.start()

# --- বটের মূল কোড ---

BOT_TOKEN = '8309490353:AAEJMzYoMCfjfUZXdIf9IW3IS9REZJDTBUk' # এখানে আপনার টোকেন দিন
CHANNEL_ID = '@fflikebd'
MAIN_CHANNEL_URL = 'https://t.me/bdmodspro'

bot = telebot.TeleBot(BOT_TOKEN)

def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except Exception:
        return False

def send_join_msg(message):
    markup = types.InlineKeyboardMarkup()
    join_button = types.InlineKeyboardButton("🚀 Join Channel to Use Bot", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")
    markup.add(join_button)
    bot.reply_to(message, f"❌ আপনি আমাদের চ্যানেলে জয়েন নেই!\n\nবটটি ব্যবহার করতে অবশ্যই {CHANNEL_ID} চ্যানেলে জয়েন হতে হবে।", reply_markup=markup)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if not is_subscribed(message.from_user.id):
        send_join_msg(message)
        return

    welcome_text = (
        "‎\n"
        "‎🔥 ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ ᴛʜᴇ ᴏᴜʀ ʙᴏᴛ 🔥\n"
        "‎\n"
        "‎ᴄᴏᴍᴍᴀɴᴅꜱ:\n"
        "‎/ᴇᴍᴏᴛᴇ <ᴛᴇᴀᴍᴄᴏᴅᴇ> <ᴜɪᴅꜱ> <ᴇᴍᴏᴛᴇɪᴅ>\n"
        "‎/5ɢ <ᴜɪᴅ>\n"
        "‎/6ɢ <ᴜɪᴅ>\n"
        "‎/ʟᴀɢ <ᴛᴇᴀᴍᴄᴏᴅᴇ>\n"
        "‎\n"
        "➥ ᴘᴏᴡᴇʀ  ʙʏ  ᴊᴜʙᴀʏᴇʀ  ♡ جباير"
    )
    
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("📢 Main Channel", url=MAIN_CHANNEL_URL)
    markup.add(btn)
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.message_handler(commands=['emote', '5g', '6g', 'lag'])
def handle_commands(message):
    if not is_subscribed(message.from_user.id):
        send_join_msg(message)
        return
    bot.reply_to(message, "⚙️ processing... (আপনার লজিক এখানে দিন)")

if __name__ == "__main__":
    print("✅ Bot system is active...")
    keep_alive() # Flask সার্ভার চালু করা
    bot.polling(none_stop=True)
