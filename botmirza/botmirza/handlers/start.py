from telebot import types
from templates import messages

def register_handlers(bot):
    @bot.message_handler(commands=['start'])
    def start_handler(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("📜 راهنما", "💳 خرید اشتراک")
        bot.send_message(message.chat.id, messages.WELCOME_FA, reply_markup=markup)
