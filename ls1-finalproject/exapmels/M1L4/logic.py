from random import randint
import requests
import datetime

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.imgshiny=self.get_imgshiny()
        self.power=randint(1,100)
        self.hp=randint(75,350)
        self.last_feed_time=datetime.datetime.now()
        Pokemon.pokemons[pokemon_trainer] = self
    def attack(self, enemy):
        if isinstance(enemy,Wizzard):
            chance=randint(1,5)
            if chance==1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    # Метод для получения картинки покемона через API
    def get_img(self):
        url=f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return(data["sprites"]["other"]["official-artwork"]["front_default"])
        
    def get_imgshiny(self):
        url=f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()   
            return(data["sprites"]["other"]["home"]["front_shiny"])
            
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Pikachu"


    # Метод класса для получения информации
    def info(self):
        return f"Имя твоего покеомона: {self.name}. HP:{self.hp}. power:{self.power}"


    # Метод класса для получения картинки покемона
    def show_img(self):
        return self.img
    def show_imgshiny(self):
        return self.imgshiny

    def feed(self, feed_interval = 20, hp_increase = 10 ):
        current_time =datetime.datetime.now()
        delta_time = datetime.timedelta(seconds=feed_interval)  
        if (current_time - self.last_feed_time) > delta_time:
            self.hp += hp_increase
            self.last_feed_time = current_time
            return f"Здоровье покемона увеличено. Текущее здоровье: {self.hp}"
        else:
            return f"Следующее время кормления покемона: {self.last_feed_time+delta_time}"  

class Wizzard(Pokemon):
    pass

class Fighter(Pokemon):
    def attack(self, enemy):
        super_power=randint(5,15)
        self.power+=super_power
        result=super().attack(enemy)
        self.power-=super_power
        return result+f"Боец применил супер-атаку силой:{super_power} "