import telebot
import json
from telebot import types
from src.strings import *

TOKEN = '5915906436:AAFtEF_PWpfz2GGvoPL8S-9GPJJ87CKEN20'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def command_start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(btn_list_summary)
    button2 = types.KeyboardButton(btn_create_summary)
    markup.add(button1, button2)
    bot.send_message(message.chat.id, start_message, reply_markup=markup)


@bot.message_handler(commands=['summary_list'])
def command_get_list_summary(message):
    bot.send_message(message.chat.id, "lst")


@bot.message_handler(commands=['create_summary'])
def command_create_summary(message):
    bot.send_message(message.chat.id, "cr")


@bot.message_handler(content_types="text")
def all_messages(message):
    if message.text == btn_list_summary:
        command_get_list_summary(message)
    elif message.text == btn_create_summary:
        command_create_summary(message)
    else:
        bot.send_message(message.chat.id, unknown_message)


bot.polling(none_stop=True)