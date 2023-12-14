import random
class Human:
    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 200
        self.enjoyment = 100
        self.home = home
        self.car = car

    def get_home(self, home):
        if home != None:
            print("продали будинок")
        self.home = home
        print("придбали будинок")

    def get_car(self, car):
        if car != None:
            print(f"Продали авто марки {car.model}")
        self.car = car
        print(f"Придбана автівка, марка {car.model}")

    def work(self):
        print("Ідем працювати")
        money = random.randint(5, 20)
        print(f"Сьогодні заробили {money}$")
        self.money += money
        self.enjoyment -= 5

    def chill(self):
        print("Відпочиваємо")
        enjoyment_gain = random.randint(5, 15)
        print(f"Відпочинок додав {enjoyment_gain} радості")
        self.enjoyment += enjoyment_gain


    def shopping(self):
        print("Йдемо на шопінг")
        cost = random.randint(10, 30)
        if cost > self.money:
            print("Не вистачає грошей на покупки!")
        else:
            print(f"Покупки вартістю {cost}$ зроблені")
            self.money -= cost
            self.enjoyment += 5
    def clean_house(self):
        print("Прибираємо вдома")
        cleanliness_gain = random.randint(5, 15)
        print(f"Прибирання підняло рівень чистоти на {cleanliness_gain}")
        self.home.cleanliness_level += cleanliness_gain
    def life(self):
        pass

    def is_alive(self):
        pass

    def info(self):
        pass


class Car:
    def __init__(self, model):
        self.model = model
        self.passengers = []

    def add_passenger(self, human):
        self.passengers.append(human)

    def passengers_info(self):
        print(f'Авто {self.model}, ', end= '')
        if self.passengers != []:
            print(f'сейчас в салоне:')
            for p in self.passengers:
                print(p.name)
        else:
            print('нет пассажиров')

class Home:
    def __init__(self):
        self.food = 0
        self.cleanliness_level = 50


human1 = Human("Sergay")
human2 = Human("Anna")
car = Car("BMW X9")
car.add_passenger(human1)
car.add_passenger(human2)
car.passengers_info()