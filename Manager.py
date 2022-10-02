from parser.JsonParser import deserialize
from parser.JsonParser import serialize
from model.User import User
from parser.XMLParser import XMLserialization
from parser.XMLParser import XMLdeserialization
import os


def print_menu():
    print("Выберете, что должна сделать программа:" + "\n" +
          "1.Загрузить данные в файл" + "\n" +
          "2.Загрузить данные с файла" + "\n" +
          "3.Добавить книгу пользователю" + "\n" +
          "4.Удалить книгу у пользователя" + "\n" +
          "5.Добавить пользователя" + "\n" +
          "6.Удалить пользователя" + "\n" +
          "7.Добавить книгу" + "\n" +
          "8.Удалить книгу" + "\n" +
          "9.Показать всех пользователей и все книги" + "\n" +
          "10.Выйти" + "\n" +
          "11.Очистить базу пользователей" + "\n"
          )


users = {}
books = {}


def save_xml():
    for key, val in books.items():
        print(val)
        XMLserialization(val)


def save_json():
    data = {}
    data["users"] = users
    serialize(data)


def load_xml():
    books[XMLdeserialization("dick.xml")[0].serial_number]=XMLdeserialization("dick.xml")[0]


def load_json():
    if os.stat("data.json").st_size != 0:
        for key, val in deserialize()["users"].items():
            users[int(key)] = User(int(key), val["name"], val["book"])
        return users


def remove_json():
    open("data.json", 'w').close()


def add_user(data):
    users[data.serial_number] = data
    books.get(1)


def remove_user(data):
    try:
        users.pop(int(data))
    except ValueError:
        print("Ошибка валидации данных")
    except KeyError:
        print("Ошибка валидации данных")


def print_all_users():
    print("Users:")
    for key, value in users.items():
        print(value.__dict__)
    print("\n")


def add_book(data):
    books[data.serial_number] = data


def remove_book(data):
    try:
        books.pop(int(data))
    except ValueError:
        print("Ошибка валидации данных")
    except KeyError:
        print("Ошибка валидации данных")


def print_all_books():
    print("Books:")
    for key, value in books.items():
        print(value.__dict__)
    print("\n")


def add_book_to_user(user, book_id):
    try:
        users.get(int(user)).book.append(books.get(int(book_id)).serial_number)
    except ValueError:
        print("Ошибка валидации данных111")
    except AttributeError:
        print("Ошибка валидации данных")


def remove_book_to_user(user, book_id):
    try:
        users.get(int(user)).book.remove(int(book_id))
    except ValueError:
        print("Ошибка валидации данных")
    except AttributeError:
        print("Ошибка валидации данных")
