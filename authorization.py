from cryptography.fernet import Fernet
from main import load_key

key = load_key()
fernet_key = Fernet(key)


def authorization(login, password, fernet_obj):
    with open("passwords.txt") as file:
        for line in file:
            if line.strip():
                stored_login, encrypted_password = line.strip().split("|")
                if stored_login == login:
                    return fernet_obj.decrypt(encrypted_password.encode()).decode() == password
    return False

while True:
    if authorization(input("Введите логин: "), input("Введите пароль: "), fernet_key):
        print("Вы авторизованы")
        break
    print("Такого пользователя нет")