import telebot
from config import BOT_TOKEN
from handlers import start, admin, representative, custom_buttons

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")

# ثبت همه هندلرها
start.register_handlers(bot)
admin.register_handlers(bot)
representative.register_handlers(bot)
custom_buttons.register_handlers(bot)

if __name__ == "__main__":
    print("🤖 Bot is running...")
    bot.infinity_polling()
