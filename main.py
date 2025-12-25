import os
from cryptography.fernet import Fernet

def write_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)

def load_key():
    with open("key.key", "rb") as key_file:
        return key_file.read()

def add_password(fernet_obj):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")

    encrypted_password = fernet_obj.encrypt(password.encode())

    with open("passwords.txt", "a") as file:
        file.write(f"{login}|{encrypted_password.decode()}\n")

def view(fernet_obj):
    if not os.path.exists("passwords.txt"):
        print("Файл с паролями не найден.")
        return

    with open("passwords.txt", "r") as file:
        for line in file:
            line = line.strip()
            if line:
                login, enc = line.split("|")
                decrypted = fernet_obj.decrypt(enc.encode()).decode()
                print(f"Логин: {login} | Пароль: {decrypted}")

def main_menu():
    write_key()
    key = load_key()
    fernet_key = Fernet(key)

    while True:
        print("\nЧто вы хотите сделать?")
        action = input("1. Посмотреть, 2. Добавить. 3. Авторизоваться. Нажмите 4 чтобы выйти: ")

        if action == "1":
            view(fernet_key)
        elif action == "2":
            add_password(fernet_key)
        elif action == "3":
            from authorization import authorize
            authorize(fernet_key)
        elif action == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main_menu()