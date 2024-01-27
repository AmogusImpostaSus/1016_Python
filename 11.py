import random

class Human:
    def __init__(self, name, home=None, car=None):
        self.name = name
        self.money = 200
        self.enjoyment = 100
        self.home = home
        self.car = car
        self.knowledge = 0
    def get_car(self, car):
        if car != None:
            print(f"Продали авто марки {car.marka}")
        self.car = car
        print(f"Придбана автівка, марка {car.marka}")

    def work(self):
        print("Ідем працювати :(")
        money = random.randint(5, 20)
        print(f"Сьогодні заробили {money}$")
        self.money += money
        self.enjoyment -= 5
        self.home.food -= 2

    def chill(self):
        print("Відпочиваємо")
        enjoyment = random.randint(3, 8)
        print(f"Ви відпочили, і почуваєтесь на всі {enjoyment}!")
        self.enjoyment += enjoyment

    def shopping(self):
        if self.car != None:
            print(f"Ідем за покупками")
        else:
            print(f"Їдемо на {self.car.marka} за покупками")

        money = random.randint(5, 20)
        print(f"я сьогодні був у магазині і витратив {money}$")
        self.money -= money
        self.home.food += random.randint(5, 10)
        self.enjoyment += random.randint(-5, 5)

    def visit_friends(self):
        print("Відвідуємо друзів")
        enjoyment = random.randint(5, 15)
        print(f"Провели час з друзями і отримали {enjoyment} радості!")
        self.enjoyment += enjoyment

    def learn(self):
        print("Вчимося новому")
        knowledge_gain = random.randint(3, 10)
        print(f"Вивчили щось нове і отримали {knowledge_gain} знань!")
        self.knowledge += knowledge_gain
        self.enjoyment += random.randint(-5, 5)

    def clean_house(self):
        if self.home == None:
            print(f"Ти не можешь прибратися")
        else:
            print("Пішли прибиратися")
            self.home.cleanlinies_level += 1
            self.enjoyment -= 3

    def go_on_vacation(self):
        cost = 150
        if self.money >= cost:
            print("Поїхали відпочивати, отримали незабутні враження!")
            self.money -= cost
            self.enjoyment += random.randint(30, 50)
        else:
            print("Недостатньо грошей для відпочинку.")

    def upgrade_home(self):
        cost = 100
        if self.money >= cost:
            print(f"Оновили свій будинок, порядок в кімнаті покращився!")
            self.money -= cost
            self.home.cleanlinies_level += 10
        else:
            print("Недостатньо грошей для оновлення будинку.")

    def buy_entertainment(self):
        cost = 30
        if self.money >= cost:
            print("Купили новий розваги, зростив рівень задоволення!")
            self.money -= cost
            self.enjoyment += random.randint(10, 20)
        else:
            print("Недостатньо грошей для купівлі розваг.")

    def life(self):

        r = random.randint(1, 9)
        if r == 1:
            self.work()
        elif r == 2:
            self.chill()
        elif r == 3:
            self.clean_house()
        elif r == 4:
            self.shopping()
        elif r == 5:
            self.visit_friends()
        elif r == 6:
            self.learn()
        elif r == 7:
            self.buy_entertainment()
        elif r == 8:
             self.go_on_vacation()
        elif r == 9:
            self.upgrade_home()


        if self.enjoyment < 5:
            self.chill()
        if self.money < 10:
            self.work()
        if self.money > 500:
            self.get_car(Car("BMW X22"))
            self.money -= 500

    def is_alive(self):
        if self.money <= 0 or self.home.food <= 0:
            return False
        return True

    def info(self):
        print("===============================")
        print(f"Стан {self.name}:")
        print(f"Рівень задоволення - {self.enjoyment}")
        print(f"Залишок грошей     - {self.money}")
        print(f"Наявність їжі      - {self.home.food}")
        print(f"Порядок в кімнаті  - {self.home.cleanlinies_level}")
        print(f"Знання             - {self.knowledge}")

class Car:
    def __init__(self, marka):
        self.marka = marka

    def upgrade_car(self):
        cost = 300
        if self.money >= cost:
            print(f"Оновили авто на {self.car.marka}, отримали нові можливості!")
            self.money -= cost
            self.car = Car("Upgraded " + self.car.marka)
        else:
            print("Недостатньо грошей для оновлення автомобіля.")

class Home:
    def __init__(self):
        self.food = 50
        self.cleanlinies_level = 50

human = Human("людини", car=Car("BMW X11"), home=Home())
day = 1
while(human.is_alive()):
    print()
    print(f"День {day}")
    human.life()
    human.info()
    day += 1
    if day > 200:
        print("Ви прожили 200 днів")
        exit(0)