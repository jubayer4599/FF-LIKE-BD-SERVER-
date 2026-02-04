import telebot
from telebot import types

# আপনার টেলিগ্রাম বটের টোকেন এখানে দিন
BOT_TOKEN = '8309490353:AAEJMzYoMCfjfUZXdIf9IW3IS9REZJDTBUk'
CHANNEL_ID = '@fflikebd'  # ফোর্স জয়েন চ্যানেল
MAIN_CHANNEL_URL = 'https://t.me/bdmodspro' # মেইন চ্যানেল লিংক

bot = telebot.TeleBot(BOT_TOKEN)

print("✅ Bot system is active...")

# মেম্বারশিপ চেক করার ফাংশন
def is_subscribed(user_id):
    try:
        status = bot.get_chat_member(CHANNEL_ID, user_id).status
        return status in ['member', 'administrator', 'creator']
    except Exception:
        return False

# জয়েন করার মেসেজ পাঠানোর ফাংশন
def send_join_msg(message):
    markup = types.InlineKeyboardMarkup()
    join_button = types.InlineKeyboardButton("🚀 Join Channel to Use Bot", url=f"https://t.me/{CHANNEL_ID.replace('@', '')}")
    markup.add(join_button)
    
    bot.reply_to(message, f"❌ আপনি আমাদের চ্যানেলে জয়েন নেই!\n\nবটটি ব্যবহার করতে অবশ্যই {CHANNEL_ID} চ্যানেলে জয়েন হতে হবে। জয়েন করে আবার কমান্ড দিন।", reply_markup=markup)

# /start এবং /help কমান্ড হ্যান্ডলার
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
        "‎ᴇxᴀᴍᴘʟᴇꜱ:\n"
        "‎/ᴇᴍᴏᴛᴇ 8921806 2799021876 124080075\n"
        "‎/5ɢ 2799021876\n"
        "‎/6ɢ 2799021876\n"
        "‎/ʟᴀɢ 9886810\n"
        "‎\n"
        "➥ ᴘᴏᴡᴇʀ  ʙʏ  ᴊᴜʙᴀʏᴇʀ  ♡ جباير"
    )
    
    # বাটন তৈরি
    markup = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton("📢 Main Channel", url=MAIN_CHANNEL_URL)
    markup.add(btn)

    bot.send_chat_action(message.chat.id, 'typing')
    bot.reply_to(message, welcome_text, reply_markup=markup)

# অন্য সব কমান্ডের জন্য চেক
@bot.message_handler(commands=['emote', '5g', '6g', 'lag'])
def handle_ff_commands(message):
    if not is_subscribed(message.from_user.id):
        send_join_msg(message)
        return
    
    # এখানে আপনার কমান্ডের মূল লজিক কাজ করবে
    bot.reply_to(message, "⚙️ Command received! Processing your request...")

# বট চালু রাখা
if __name__ == "__main__":
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"Error: {e}")
