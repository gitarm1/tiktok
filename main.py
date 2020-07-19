import get_video_NoWatermark
import telebot
import config
import os
from datetime import datetime

bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.from_user.id, """Привет!
Я умею стирать водяные знаки с видео в TikTok.
Просто пришли мне ссылку на видео!""")

@bot.message_handler(content_types=['text'])
def messages(message):
    try:
        if message.text[7] == "/":
            print(str(datetime.now().time()),"|", message.text)
            name = get_video_NoWatermark.getvideo(message.text)
        while True:
            path = "download_videos/" + name
            if not os.path.exists(path):
                continue
            else:
                video = open(path, 'rb')
                bot.send_video(message.from_user.id, video)
                print(str(datetime.now().time()), "|", "Видео Отправленно!")
                os.remove(path)
                break
    except Exception as e:
        pass
bot.polling(none_stop=True) #run
