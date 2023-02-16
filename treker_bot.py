import telebot
#from telebot import apihelper
import time
import os

TOKEN = ''

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # if message.chat.type == "private":
    text = 'Привет, путешественник! Я телебот - твой помощник на этом трекинге. Я могу подсказать, в правильном ли направлении ты двигаешься. Получи карту маршрута командой /setmap Сфотографируй каждую новую локацию, стоя ПЕРЕД ней, и пришли мне. Я определю, в правильном ли направлении ты движешься. Если ты хочешь узнать обо всех моих возможностях, набери /help'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['help'])
def send_welcome(message):

    text = '''
    Доступные команды:
    /getmap - Получить карту маршрута
    /getone - Получить описание 1й локации
    /gettwo - Получить описание 2й локации
    /getthree - Получить описание 3й локации
    /getfour - Получить описание 4й (последней) локации
    /theend - Получи приз, если правильно нашел все локации'''

    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['getmap'])
def get_map(message):

    # Передаем карту маршрута. На карте отмечены 4 локации, которые нужно посетить и отправить их фото через бот
    with open('map.jpg', 'rb') as data:
        bot.send_photo(message.chat.id, data)


@bot.message_handler(commands=['getone'])
def send_welcome(message):
    # Описание 1й локации
    text = '''

    '''

    bot.send_message(message.chat.id, text)

# Пользователь отправляет боту 1е фото. Бот отправляет фото в НС, которая определяет на ту ли локацию пришел пользователь. Бот отправляет пользователю ответ НС

# TODO как отправить пользователю ответ. можно как ответ на фото или просто ответ, тк название фото м.б.разное
# TODO прописать логику, если НС ответила, что локация не та



@bot.message_handler(commands=['gettwo'])
def send_welcome(message):
    # Описание 2й локации
    text = '''
    
    '''

    bot.send_message(message.chat.id, text)

# Пользователь отправляет боту 2е фото. Бот отправляет фото в НС, которая определяет на ту ли локацию пришел пользователь. Бот отправляет пользователю ответ НС

# TODO как отправить пользователю ответ. можно как ответ на фото или просто ответ, тк название фото м.б.разное
# TODO прописать логику, если НС ответила, что локация не та


@bot.message_handler(commands=['getthree'])
def send_welcome(message):
    # Описание 3й локации
    text = '''

    '''

    bot.send_message(message.chat.id, text)

# Пользователь отправляет боту 3е фото. Бот отправляет фото в НС, которая определяет на ту ли локацию пришел пользователь. Бот отправляет пользователю ответ НС

# TODO как отправить пользователю ответ. можно как ответ на фото или просто ответ, тк название фото м.б.разное
# TODO прописать логику, если НС ответила, что локация не та


@bot.message_handler(commands=['getfour'])
def send_welcome(message):
    # Описание 4й локации
    text = '''

    '''

    bot.send_message(message.chat.id, text)

# Пользователь отправляет боту 4е фото. Бот отправляет фото в НС, которая определяет на ту ли локацию пришел пользователь. Бот отправляет пользователю ответ НС

# TODO как отправить пользователю ответ. можно как ответ на фото или просто ответ, тк название фото м.б.разное
# TODO прописать логику, если НС ответила, что локация не та




@bot.message_handler(content_types=['text'])
def hello(message):
    # если пользователь написал приветствие
    if 'привет' or 'ghbdtn' or 'hi' in message.text.lower():
        bot.reply_to(message, 'Привет, путешественник! Я телебот - твой помощник на этом трекинге. Я могу подсказать, в правильном ли направлении ты двигаешься. Получи карту маршрута командой /setmap Сфотографируй каждую новую локацию, стоя ПЕРЕД ней, и пришли мне. Я определю, в правильном ли направлении ты движешься. Если ты хочешь узнать обо всех моих возможностях, набери /help')
        #return

@bot.message_handler(content_types=['sticker'])
def send_sticker(message):
    # если пользователь отправил стикер
    FILE_ID = 'CAACAgIAAxkBAAMiXlE-A9AvsY27-I5LVYdJi3flfbwAAjoAAztgJBTc8ZnqHbRR3xgE'
    bot.send_sticker(message.chat.id, FILE_ID)
    #print(message)

@bot.message_handler(commands=['about'])
def send_about(message):
    bot.send_message(message.chat.id, "Университет искуственного интеллекта \n Anastasia Makarova (C)")


bot.polling()
