import telebot 
from config import token
from random import randint
from telebot import types
import time

bot = telebot.TeleBot(token) 
url="https://upload.wikimedia.org/wikipedia/commons/thumb/4/41/Flag_of_India.svg/1280px-Flag_of_India.svg.png"
url2="https://upload.wikimedia.org/wikipedia/en/thumb/b/ba/Flag_of_Germany.svg/800px-Flag_of_Germany.svg.png"
url3="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b1/Flag_of_San_Marino.svg/640px-Flag_of_San_Marino.svg.png"
url4="https://upload.wikimedia.org/wikipedia/commons/thumb/4/4b/Flag_of_Chad.svg/2000px-Flag_of_Chad.svg.png"
point=0
print(point)
time.sleep(1)
point+=1

print(point)
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Japan")
    item2 = types.KeyboardButton("China")
    item3 = types.KeyboardButton("India")
    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id,text="nice, lets start")
    time.sleep(2)
    bot.send_photo(message.chat.id,url)
    bot.send_message(message.chat.id,text="what a country", reply_markup=markup) 

@bot.message_handler(func=lambda message: message.text == "India" or message.text == "China" or message.text == "Japan" )
def lets_go(message):
    if message.text=="India":
        bot.send_message(message.chat.id,text="great work")
        point=+10
    else:
        bot.send_message(message.chat.id,text="No !!!!!! ITS INDIA !!!!!!!!")
        point=-5
    bot.send_message(message.chat.id,text=f"you have {point} point")
    time.sleep(2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Germany")
    item2 = types.KeyboardButton("France")
    item3 = types.KeyboardButton("Spain")
    markup.add(item1, item2, item3)

    bot.send_photo(message.chat.id,url2)
    bot.send_message(message.chat.id,text="what a country", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Germany" or message.text == "France" or message.text == "Spain" )
def lets_go2(message):
    if message.text=="Germany":
        bot.send_message(message.chat.id,text="great work")
        point=+10
    else:
        bot.send_message(message.chat.id,text="No !!!!!! ITS GERMANY !!!!!!!!")
        point=-10
    bot.send_message(message.chat.id,text=f"you have {point} point")
    time.sleep(2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("San marino")
    item2 = types.KeyboardButton("Vatican")
    item3 = types.KeyboardButton("Monaco")
    markup.add(item1, item2, item3)

    bot.send_photo(message.chat.id,url3)
    bot.send_message(message.chat.id,text="what a country", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "San marino" or message.text == "Vatican" or message.text == "Monaco" )
def lets_go3(message):
    if message.text=="San marino":
        bot.send_message(message.chat.id,text="great work")
        point=+10
    else:
        bot.send_message(message.chat.id,text="No !!!!!! ITS SAN MARINO !!!!!!!!")
        point=-10
    bot.send_message(message.chat.id,text=f"you have {point} point")
    time.sleep(2)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Colombia")
    item2 = types.KeyboardButton("Romania")
    item3 = types.KeyboardButton("Chad")
    markup.add(item1, item2, item3)

    bot.send_photo(message.chat.id,url4)
    bot.send_message(message.chat.id,text="what a country", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "Colombia" or message.text == "Romania" or message.text == "Chad" )
def lets_go4(message):
    if message.text=="Chad":
        bot.send_message(message.chat.id,text="great work")
        point=+10
    else:
        bot.send_message(message.chat.id,text="No !!!!!! ITS CHAD !!!!!!!!")
        point=-10
    bot.send_message(message.chat.id,text=f"you have {point} point")
@bot.message_handler(commands=["logo"])
def logo(message):
    photos=bot.get_user_profile_photos(message.chat.id)
    bot.send_photo(message.chat.id,photos.photos[0][0].file_id)

@bot.message_handler(commands=["question"])
def quest(message):
    bot.send_poll(message.chat.id, question="who are you",options=["ok","fine","bad"] ,allows_multiple_answers=True)

@bot.message_handler(commands=["laliga"])
def sushi (message):
    randreal=randint(50,98)
    randbar=randint(55,90)
    ranatma=randint(40,80)
    randbetiz=randint(25,57)
    randcadiz=randint(15,45)
    randrealsoc=(20,45)

    bot.send_message(message.chat.id,text=f"real madrid - {randreal} \n barcelona - {randbar}\n atletico madrid - {ranatma}\n real betiz - {randbetiz}\n cadiz - {randcadiz}\n 3real sociadad - {randrealsoc}" )


bot.infinity_polling(none_stop=True)