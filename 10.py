import sqlite3
connection = sqlite3.connect(database= "db_user.sl3", timeout = 5)
cur = connection.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Users (id integer primary key autoincrement not null, login TEXT, password TEXT);")

connection.commit()
connection.close()


def login():
    print("Меню входу")
    log = input("Введите логин: ")
    passw = input("Введите пароль: ")
    connection = sqlite3.connect(database="db_user.sl3", timeout=5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE login='{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        print("Такого пользователя не существует!")
        exit(0)
    else:
        res = list(res[0])
        if res[2] == passw:
            print("Вы зашли")
            print(f"Добро пожаловать, {log}!")

            while True:
                print("\nВыберите действие:")
                print("1. Просмотр профиля")
                print("2. Изменить пароль")
                print("3. Выход")

                choice = input("> ")

                if choice == "1":
                    print("\nПрофиль пользователя:")
                    print(f"Логин: {log}")
                    # Здесь вы можете добавить вывод других данных профиля
                elif choice == "2":
                    new_pass = input("Введите новый пароль: ")
                    cur.execute(f"UPDATE Users SET password='{new_pass}' WHERE login='{log}';")
                    connection.commit()
                    print("Пароль успешно изменен!")
                elif choice == "3":
                    print("Выход из аккаунта.")
                    break
                else:
                    print("Неверный выбор. Пожалуйста, выберите снова.")
        else:
            print("He верный логин или пароль!")
            exit(0)

def register():
    print("Меню регестрации")
    log = input("Введите логин: ")
    connection = sqlite3.connect(database="db_user.sl3", timeout=5)
    cur = connection.cursor()
    cur.execute(f"SELECT * FROM Users WHERE login = '{log}';")
    connection.commit()
    res = cur.fetchall()
    if len(res) == 0:
        passw = input("Введите пароль: ")
        cur.execute(f"INSERT INTO Users (login,password) VALUES ('{log}', '{passw}');")
        connection.commit()
        print("Успешно")
    else:
        print("Такой логин уже есть")
        exit(0)

choise = int(input("1. Войти\n2. Зарегестрироватся\n>"))
if choise == 1:
    login()
elif choise == 2:
    register()
else:
    print("не верный вариант")
    exit(0)