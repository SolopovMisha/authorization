from cryptography.fernet import Fernet
from main import load_key

def authorize(fernet_obj):
    while True:
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        
        try:
            with open("passwords.txt", "r") as file:
                for line in file:
                    line = line.strip()
                    if line:
                        stored_login, encrypted_password = line.split("|")
                        if stored_login == login:
                            decrypted_password = fernet_obj.decrypt(encrypted_password.encode()).decode()
                            if decrypted_password == password:
                                print("Вы авторизованы")
                                return True
        except FileNotFoundError:
            print("Файл с паролями не найден")
            return False
        
        print("Такого пользователя нет или пароль неверен")

def main():
    key = load_key()
    fernet_key = Fernet(key)
    authorize(fernet_key)

if __name__ == "__main__":
    main()