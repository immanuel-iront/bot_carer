import telebot 
from config import token
from telebot import types
import time
from logic import *
from collections import Counter


user_data={}
all_answers_number=[]

bot = telebot.TeleBot(token)
@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message,text="""bot commands: 
                /start-show buttons  
                /find carear road
                /productivity tips  """)
    

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("questions for starting new carear road")
    item2=types.KeyboardButton("exampels for carear roads")
    item3=types.KeyboardButton("productivity tips")
    markup.add(item1,item2,item3 )
    bot.send_message(message.chat.id,text="what you choose?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "productivity tips")
def productivity_tips_fun(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
    item1 = types.KeyboardButton("genarete productivity tip")
    item2=types.KeyboardButton("genarete motivation image")
    item3=types.KeyboardButton("back to main menu")
    markup.add(item1,item2,item3)
    bot.send_message(message.chat.id,text=" do you want to genarate productivity tip or motivation image?", reply_markup=markup)


@bot.message_handler(func=lambda message: message.text == "genarete motivation image")
def genarete_motivation_image(message):
    bot.send_photo(message.chat.id,motivations_images())
    time.sleep(5)
    productivity_tips_fun(message)


@bot.message_handler(func=lambda message: message.text == "genarete productivity tip")
def productivity_tips_genarate(message):
    bot.send_message(message.chat.id,text=Recommendations_for_improving_productivity())
    time.sleep(5)
    productivity_tips_fun(message)


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
    try:
        questions_all=list(carear_questions())
        index=user_data[chat_id]["currect question"]
        print(f"[send_question] Index: {index}, Total: {len(questions_all)}")
        if index >= len(questions_all):
            bot.send_message(chat_id , "thanks for cmopleting the test")
            get_final_result(chat_id)
        
        question=questions_all[index]
        options=questions[question]
        mrkup=types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True )
        row = []
        for  i, option in enumerate(options):
            row.append(types.KeyboardButton(option))
            if len(row) == 2: 
                mrkup.row(*row)
                row = [] 
        bot.send_message(chat_id,question,reply_markup=mrkup)
    except:
        pass

    
    


@bot.message_handler(func=lambda message: message.chat.id in user_data and "currect question" in user_data[message.chat.id] )
def get_answers(message):
    chat_id=message.chat.id
    global all_answers_number
    answer=message.text.split()[0]
    all_answers_number.append(answer)
    print(answer)
    user_data[chat_id]["answers"].append(message.text)
    user_data[chat_id]["currect question"]+=1
    bot.send_chat_action(message.chat.id, 'typing') 
    time.sleep(2)
    send_question(chat_id)

def get_final_result(chat_id):
    counter=""
    counter=Counter(all_answers_number)
    print(counter)
    most_number=max(counter.values())
    two_most_numbers = [k for k, v in counter.items() if v == most_number]
    print(two_most_numbers)
    if len(two_most_numbers) > 1:
        selected = random.choice(two_most_numbers)
    else:
        selected = two_most_numbers[0]

    if selected=="1":
        bot.send_message(chat_id,text=f"""you are 🌿 The Nature Adventurer
                You love freedom, nature, and movement. It’s important for you to feel connected to your environment, and you’re drawn to\n
                              experiences that involve adventure and physical challenges.
                            Fields that involve field exploration, hiking, sports, or anything that gives you a sense of aliveness would suit you well.""")


    elif selected=="2":
        bot.send_message(chat_id,text=f"""you are 🎨 The Creative Creator 
Your world is full of ideas and imagination. You’re drawn to creation, art, and innovation — whether through writing, drawing, or inventing. Places where you can express yourself and bring new ideas to life are where you’ll feel most at home.""")
                        
            
    elif selected=="3":
        bot.send_message(chat_id,text=f"""you are 🤝 The Social One 
Relationships and shared experiences are at the center of your life. You’re a people person — you love being surrounded by friends and building connections. Environments with collaboration, group leadership, or work that brings people together would fit you well.""")
    
    elif selected== "4" :
        bot.send_message(chat_id,text=f"""you are 📚 The Quiet Researcher 
You’re drawn to depth, knowledge, and learning. Often you’ll prefer quiet and reflection over noise and adventure. Research, teaching, science, or academic writing could suit you — any field that allows you to dive deep and explore in depth.""")
    start(chat_id)       
         


bot.remove_webhook()
bot.infinity_polling(none_stop=True)


