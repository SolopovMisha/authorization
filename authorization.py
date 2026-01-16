from cryptography.fernet import Fernet
from main import load_key


def authorize(fernet_obj):
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        
        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    if line.strip() and line.split("|")[0] == login and fernet_obj.decrypt(line.split("|")[1].encode()).decode() == password:
                        print("Вы авторизованы")
                        return True
        except FileNotFoundError:
            print("Файл с паролями не найден")
            return False
        
        print("Такого пользователя нет или пароль неверен")


def main():
    authorize(Fernet(load_key()))


if __name__ == "__main__":
    main()