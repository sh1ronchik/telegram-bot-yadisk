import telebot
from telebot import types

bot = telebot.TeleBot('7184614153:AAEFENuyy2d5K9sS7Cwi-jAC7LndzlvKn70')

@bot.message_handler(commands=['start'])
def send_welcome(message):

    keyboard = types.InlineKeyboardMarkup()

    button_os = types.InlineKeyboardButton('Git', callback_data='os')
    button_alg = types.InlineKeyboardButton('Алгоритмы и структуры данных', callback_data='alg')
    button_ass = types.InlineKeyboardButton('Ассемблер', callback_data='ass')


    keyboard.add(button_os)
    keyboard.add(button_alg)
    keyboard.add(button_ass)

    bot.reply_to(message, "Привет, какая дисциплина тебя интересует?", reply_markup=keyboard)


bot.infinity_polling()