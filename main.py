import telebot
from telebot import types
import os
import random as rd


bot = telebot.TeleBot('5156000134:AAHnC8amzGsymHCsdgAnH-KGa1pQFNmrs0A')
markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
markup.add(types.KeyboardButton("[Пердёж]"))

farts_ways = []
for dirpath, dirnames, filenames in os.walk('files/audio/farts'):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        farts_ways.append(file_path)


@bot.message_handler(commands=['buttons', 'start'])
def button_message(message):
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.chat.id, 'Команды:\n/help\n/buttons')

    elif message.text == "[Пердёж]":
        bot.send_audio(message.chat.id, open(rd.choice(farts_ways), mode='rb'))

    elif message.text == "привет":
        bot.send_message(message.chat.id, 'привет')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")


bot.infinity_polling()
