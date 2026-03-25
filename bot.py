import telebot

TOKEN = "8681271948:AAEG4JniBi_GSxeOxxeQY85HYCow-7QporI"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = """សួស្តី👋
សូមស្វាគមន៍មកកាន់ STN Support Bot 🤖
ទទួលបានព័ត៌មានថ្មីៗ ការណែនាំ និងព័ត៌មានមានប្រយោជន៍ក្នុងកន្លែងតែមួយ។
សម្រាប់ព័ត៌មានបន្ថែម សូមចូលទៅកាន់ @Cockstn03TT 🚀
"""
    bot.reply_to(message, welcome_text)

bot.infinity_polling()
