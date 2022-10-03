from parser.JsonParser import deserialize
from parser.JsonParser import serialize
from model.User import User
from parser.XMLParser import XMLserialization
from parser.XMLParser import XMLdeserialization
from model.Book import Book
from exception.NonFindException import NonFindException


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
          "11.Очистить базу пользователей" + "\n" +
          "12.Обновить пользователя" + "\n" +
          "13.Обновить книгу" + "\n"
          )


users = {}
books = {}


def save_xml(path):
    data = []
    for key, val in books.items():
        data.append(val.__dict__)
    XMLserialization(data, path)


def save_json(path):
    data = {}
    for key, val in users.items():
        users[key] = val.__dict__
    data["users"] = users
    serialize(data, path)


def load_xml(data):
    try:
        for el in XMLdeserialization(data):
            books[el.serial_number] = el
    except FileNotFoundError:
        print("Не удается найти указанный файл: " + data)
    except TypeError:
        print("Не удается найти указанный файл: " + data)


def load_json(data):
    try:
        for key, val in deserialize(data)["users"].items():
            users[int(key)] = User(int(key), val["name"], val["book"])
        return users
    except FileNotFoundError:
        print("Не удается найти указанный файл: " + data)
    except TypeError:
        print()


def remove_json():
    open("data.json", 'w').close()


def add_user(data):
    users[data.serial_number] = data


def remove_user(data):
    users.pop(int(data))


def print_all_users():
    print("Users:")
    for key, value in users.items():
        print(value.__dict__)
    print("\n")


def add_book(data):
    books[data.serial_number] = data


def remove_book(data):
    books.pop(int(data))



def print_all_books():
    print("Books:")
    for key, value in books.items():
        print(value.__dict__)
    print("\n")


def add_book_to_user(user, book_id):
    users.get(user).book.append(books.get(book_id).serial_number)


def remove_book_to_user(user, book_id):
    users.get(int(user)).book.remove(int(book_id))


def update_user(user_id, data):
    a=users.get(user_id).book
    data.book=a
    users[user_id] = data


def update_book(book_id, data):
    books[book_id] = data


def is_user_exist(data):
    if users.get(data, None) is None:
        return False
    else:
        return True


def is_book_exist(data):
    if books.get(data, None) is None:
        return False
    else:
        return True
