import os
from cryptography.fernet import Fernet

def write_key():
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
        print("Ключ создан")
    else:
        print("Ключ уже создан.")


def load_key():
    with open("key.key", "rb") as key_file:
        key = key_file.read()
    print(f"Ключ из файла: {key.decode()}")
    return key


def add_password(fernet_obj):
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    
    encrypted_password = fernet_obj.encrypt(password.encode())
    
    with open("passwords.txt", "a") as file:
        file.write(f"{login}|{encrypted_password.decode()}\n")
    
    print("Готово!")


def view(fernet_obj):
    for line in open("passwords.txt"):
        if line.strip():
            login, enc = line.strip().split("|")
            print(f"Логин: {login} | Пароль: {fernet_obj.decrypt(enc.encode()).decode()}")


if __name__ == "__main__":
    write_key()
    key = load_key()
    fernet_key = Fernet(key)

    while True:
        print("\nХотите добавить новый пароль или посмотреть уже существующие?")
        action = input("1. Посмотреть, 2. Добавить. 3. Авторизоваться. Нажмите 4 чтобы выйти: ")

        if action == "1":
            view(fernet_key)
        elif action == "2":
            add_password(fernet_key)
        elif action == "3":    
            import authorization       
        elif action == "4":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")