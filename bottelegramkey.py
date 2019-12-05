import telebot
bot = telebot.TeleBot('826609662:AAEuZX9v53NkvN-HiL-tBSrly9rH10wm0Xg')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()
