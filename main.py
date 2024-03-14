import telebot
from telebot import types

bot = telebot.TeleBot('7184614153:AAEFENuyy2d5K9sS7Cwi-jAC7LndzlvKn70')

def create_main_keyboard():
    keyboard_main = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        types.KeyboardButton('Git'),
        types.KeyboardButton('Алгоритмы и структуры данных'),
        types.KeyboardButton('Ассемблер')
    ]
    keyboard_main.add(*buttons)
    return keyboard_main

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard_main = create_main_keyboard()
    bot.send_message(message.chat.id, "Привет, выбери интересующую тебя дисциплину:", reply_markup=keyboard_main)

@bot.message_handler(func=lambda message: True)
def handle_choice(message):
    try:
        if message.text == 'Git':
            keyboard = types.InlineKeyboardMarkup()
            url_button = types.InlineKeyboardButton(text="Перейти", url="https://disk.yandex.ru/d/FQF3XaoDUh_jbg/git")
            keyboard.add(url_button)
            bot.send_message(message.chat.id, "Материал по дисциплине 'Git':", reply_markup=keyboard)
        elif message.text in ['Алгоритмы и структуры данных', 'Ассемблер']:
            bot.send_message(message.chat.id, f"Материал по дисциплине '{message.text}':")
        else:
            bot.send_message(message.chat.id, "Неизвестный выбор. Пожалуйста, выберите одну из предложенных дисциплин.")
    except Exception as e:
        bot.send_message(message.chat.id, "Произошла ошибка. Пожалуйста, попробуйте снова.")

if __name__ == '__main__':
    bot.infinity_polling()