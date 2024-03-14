import telebot
from telebot import types

bot = telebot.TeleBot('7184614153:AAEFENuyy2d5K9sS7Cwi-jAC7LndzlvKn70')

@bot.message_handler(commands=['start'])
def send_welcome(message):

    keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)

    button_git = types.KeyboardButton('Git')
    button_alg = types.KeyboardButton('Алгоритмы и структуры данных')
    button_ass = types.KeyboardButton('Ассемблер')


    keyboard_main.add(button_git, button_alg, button_ass)

    bot.send_message(message.chat.id, "Привет, выбери интересующую тебя дисциплину:", reply_markup=keyboard_main)

@bot.message_handler(func=lambda message: message.text == "Git")
def choice_button_git(message):
    bot.send_message(message.chat.id, "Материал по Git:")

@bot.message_handler(func=lambda message: message.text == "Алгоритмы и структуры данных")
def button1(message):
    bot.send_message(message.chat.id, "Материал по алгоритмам и структурам данных:")

@bot.message_handler(func=lambda message: message.text == "Ассемблер")
def button1(message):
    bot.send_message(message.chat.id, "Материал по ассемблеру:")


if __name__ == '__main__':
    bot.infinity_polling()