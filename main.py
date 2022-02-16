import telebot
from telebot import types


bot = telebot.TeleBot('5156000134:AAHnC8amzGsymHCsdgAnH-KGa1pQFNmrs0A')
markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
markup.add(types.KeyboardButton("[Кнопка]"))
markup.add(types.KeyboardButton("Кнопка2"))


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'команда start')


@bot.message_handler(commands=['buttons'])
def button_message(message):
    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/help":
        bot.send_message(message.chat.id, 'Команды:\n/help\n/buttons')
    elif message.text == "[Кнопка]":
        bot.send_message(message.chat.id, 'Вы нажали на кнопку')
    elif message.text == "привет":
        bot.send_message(message.chat.id, 'привет')
    else:
        bot.send_message(message.chat.id, "Я тебя не понимаю. Напиши /help.")


bot.infinity_polling()
