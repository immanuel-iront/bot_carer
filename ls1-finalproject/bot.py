import telebot 
from config import token
from telebot import types
import time
from logic import *

user_data={}

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,text="""bot commands: 
                /start-show buttons  
                /find carear road """)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("questions for starting new carear road")
    item2=types.KeyboardButton("exampels for carear roads")
    markup.add(item1,item2 )
    bot.send_message(message.chat.id,text="what you choose?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "exampels for carear roads" )
def exampels_for_carear_roads_bot(message):
    bot.send_message(message.chat.id,text=exampels_for_carear_roads())

@bot.message_handler(func=lambda message: message.text == "questions for starting new carear road" )
def start_newcarer_main(message):
    bot.send_message(message.chat.id,text="you choose to start a new carear! let'ts answer to a few questions")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("let'ts try")
    item2=types.KeyboardButton("back to main menu")
    markup.add(item1,item2 )
    bot.send_message(message.chat.id,text="do you ready for start?", reply_markup=markup)

@bot.message_handler(func=lambda message: message.text == "back to main menu" )
def start_new_carear_questions(message):
    start(message)



@bot.message_handler(func=lambda message: message.text == "let'ts try" )
def start_quiz(message):
    chat_id=message.chat.id
    user_data[chat_id]={
        "currect question": 0 ,
        "answers": []
    }
    send_question(chat_id)


def send_question(chat_id):
    questions_all=list(carear_questions())
    index=user_data[chat_id]["currect question"]
    if index >= len(carear_questions()):
        bot.send_message(chat_id , "thanks for cmopleting the test")
        return 
    question=questions_all[index]
    options=questions[question]
    mrkup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    for i in options:
        mrkup.add(types.KeyboardButton(i))
    bot.send_message(chat_id,questions,reply_markup=mrkup)


@bot.message_handler(func=lambda message: message.chat.id in user_data and "currect question" in user_data[message.chat.id] )
def get_answers(message):
    chat_id=message.chat.id
    user_data[chat_id]["answers"].append(message.text)
    user_data[chat_id]["currect question"]+=1
    send_question(chat_id)

bot.infinity_polling(none_stop=True)


