import telebot 
from config import token
from random import randint
from logic import Pokemon, Wizzard,Fighter

bot = telebot.TeleBot(token) 

@bot.message_handler(commands=['go'])
def go(message):
    if message.from_user.username not in Pokemon.pokemons.keys():
        chance = randint(1,3)
        if chance == 1:
            pokemon = Pokemon(message.from_user.username)
        elif chance == 2:
            pokemon = Wizzard(message.from_user.username)
        elif chance == 3:
            pokemon = Fighter(message.from_user.username)
        shiny=randint(1,20)
        if shiny==1 :
            bot.send_message(message.chat.id, pokemon.info())
            bot.send_photo(message.chat.id, pokemon.show_imgshiny())
            bot.send_message(message.chat.id, "you got shiny pokemon")
        else:
            bot.send_message(message.chat.id, pokemon.info())
            bot.send_photo(message.chat.id, pokemon.show_img())
       
    else:
        bot.reply_to(message, "Ты уже создал себе покемона")

@bot.message_handler(commands=["pokemon"])
def pokem(message):
    pokemon = Pokemon(message.from_user.username)
    shiny=randint(1,50)
    if shiny==1 :
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_imgshiny())
        bot.send_message(message.chat.id, "✨you got shiny pokemon✨")
    else:
        bot.send_message(message.chat.id, pokemon.info())
        bot.send_photo(message.chat.id, pokemon.show_img())

        
@bot.message_handler(commands=['attack'])
def attack_pok(message):
    if message.reply_to_message:
        if message.reply_to_message.from_user.username in Pokemon.pokemons.keys() and message.from_user.username in Pokemon.pokemons.keys():
            enemy = Pokemon.pokemons[message.reply_to_message.from_user.username]
            pok = Pokemon.pokemons[message.from_user.username]
            res = pok.attack(enemy)
            bot.send_message(message.chat.id, res)
        else:
            bot.send_message(message.chat.id, "Сражаться можно только с покемонами")
    else:
            bot.send_message(message.chat.id, "Чтобы атаковать, нужно ответить на сообщения того, кого хочешь атаковать")

@bot.message_handler(commands=["info"])
def info_pok(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id, pok.info())
    else:
         bot.reply_to(message, "you dont have a pokemon")
    
        
@bot.message_handler(commands=["feed"])
def feed(message):
    if message.from_user.username in Pokemon.pokemons.keys():
        pok = Pokemon.pokemons[message.from_user.username]
        bot.send_message(message.chat.id,pok.feed() )
    else:
         bot.reply_to(message, "you dont have a pokemon")
    


bot.infinity_polling(none_stop=True)

