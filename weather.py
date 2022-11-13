import telebot
import random
from random import randint
from pyowm import OWM
from pyautogui import screenshot
import os
from pathlib import Path
import asyncio
import time
import shutil
import playsound

bot = telebot.TeleBot('5631167448:AAF653atpU0mAOvrOknu30_YC9YtvcS-7Ms')
id_gruppi = '-1001641413207'
papkaggg = 'C:\\Users\\Provonsal\\Downloads\\ggg\\'
papkagovno = 'D:\\русификатор\\gavno\\'
city = 'Новосибирск'
sound = 'audio.wav'
@bot.message_handler(func=lambda message: message.text == "Скриншот")
def msg(message):
    playsound.playsound(sound)
    def photog(doc_name):
        bot.send_document(message.chat.id, open(doc_name, 'rb'))
    scr = screenshot('screen.jpg')
    photog('screen.jpg')
    
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Список доступных команд:\n /ran \n /weather \n /screen")

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width = 1)
    button_scr = telebot.types.KeyboardButton('Скриншот')
    button_weather = telebot.types.KeyboardButton('Погода')
    button_random = telebot.types.KeyboardButton('Вероятность')
    
    markup.add(button_scr, button_weather, button_random)
    #mess = f'Привет, {message.from_user.first_name} {message.from_user.last_name}\nСписок доступных команд:\n /ran \n /weather \n /screen'
    bot.send_message(message.chat.id, 'Лиза лучшая мама', reply_markup = markup)
    
@bot.message_handler(commands=['test'])
def test(message):
    bot.send_message(id_gruppi, "ХУЙ ХУЙ")

@bot.message_handler(func=lambda message: message.text == "Вероятность")
def veroyatnost(message):
    bot.send_message(message.chat.id, f"{message.from_user.first_name}, вероятность составляет: {randint(0, 100)}%", parse_mode='html')

@bot.message_handler(func=lambda message: message.text == "Погода")
def weather1(message):
    def weather():
        owm = OWM('15c4cba72e9ba577c9edff169b2a41be')
        mgr = owm.weather_manager()
        observation = mgr.weather_at_place(city)
        weather = observation.weather
        temperature = weather.temperature("celsius")
        print(temperature)
        return temperature
    w = weather()
    bot.send_message(message.chat.id, f'В городе {city} сейчас {round(w["temp"])} градусов, чувствуется как {round(w["feels_like"])} градусов')
@bot.message_handler(commands=['пикчи'])
def arts(message):
    arti = os.listdir("C:\\Users\\Provonsal\\Downloads\\ggg")    
    medias = []
    
    def otpravka(message):
        b = 0
        medias = []
        for i in arti:
                if os.stat(f'{papkaggg}{i}').st_size > 60000000:
                    bot.send_message(message.chat.id, f'Этот файл слишком большой {i}.\nСлишком большие файлы не будут отправлены. Отправь вручную.\nНапиши /го и все файлы кроме больших переместятся.')
                elif Path(f'{papkaggg}{i}').suffix == '.mp4' or Path(f'{papkaggg}{i}').suffix == '.webm':
                    bot.send_video(id_gruppi, open(f'{papkaggg}{i}', 'rb'))
                elif Path(f'{papkaggg}{i}').suffix == '.gif':
                    bot.send_document(id_gruppi, open(f'D:\\{papkaggg}{i}', 'rb'))
                elif Path(f'{papkaggg}{i}').suffix == '.png' or Path(f'{papkaggg}{i}').suffix == '.jpg' or Path(f'{papkaggg}{i}').suffix == '.jpeg':
                    medias.append(telebot.types.InputMediaPhoto(open(f'{papkaggg}{i}', 'rb')))
                    b = b + 1
                    #bot.send_message(message.chat.id, f'пум. {i}')
                    while b == 10:
                        try:
                            #bot.send_message(message.chat.id, 'Пум.')
                            bot.send_media_group(id_gruppi, medias) 
                            b = 0
                            medias = []
                        except:
                            bot.send_message(message.chat.id, f'Хуйня: {i}')
        bot.send_message(message.chat.id, f'Отправка пикч завершена')
    otpravka(message)
        
@bot.message_handler(commands=['го'])
def peremeshenie(message): 
    arti = os.listdir("C:\\Users\\Provonsal\\Downloads\\ggg")
    for i in arti:
        if os.stat(f'{papkaggg}{i}').st_size < 52428800:
            shutil.move(f'{papkaggg}{i}', f"{papkagovno}{i}")
        else:
            bot.send_message(message.chat.id, f'Тяжелый файл для бота.\n"{i}" \nСлишком тяжелые файлы остануться в папке для самостоятельной отправки.')
    bot.send_message(message.chat.id, 'Файлы успешно перемещены.')
    

    
    


bot.polling(none_stop= True)
