# -*- coding: utf-8 -*-
import telebot
from telebot import apihelper

apihelper.proxy = {'https': 'socks5://rkn:9ophEgTa@rkn.pizd.ec:443'}

bot = telebot.TeleBot("607107519:AAHDGXPtlh9McqYNqdiPFTzIFFcESOL5_UQ")


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    msg = bot.send_message(message.chat.id, 'Привет! Я codex_bot!')


@bot.message_handler(commands=['auth'])
def send_auth(message):
    pass


bot.polling()
