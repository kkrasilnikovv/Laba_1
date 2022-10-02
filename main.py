from Manager import *
from model.User import User
from model.Book import Book

count = 0
count1 = 0
print_menu()
while True:
    a = input()
    if a == '1':
        save_json()
        save_xml()
    elif a == '2':
        print("Был создан жесткий костыль,но это был единственный выход")
        try:
            count = load_json().__len__()
        except AttributeError:
            print("Файл для загрузки пустой")
        try:
            load_xml()
        except FileNotFoundError:
            print("Неверно указан путь к файлу")

    elif a == '3':
        print("Введите id пользователя")
        user = input()
        print("Введите id книги")
        id = input()
        add_book_to_user(user, id)
    elif a == '4':
        print("Введите id пользователя")
        user = input()
        print("Введите id книги")
        id = input()
        remove_book_to_user(user, id)
    elif a == '5':
        print("Введите имя пользователя")
        name = input()
        if not name.isalpha():
            print("Ошибка валидации данных")
        else:
            add_user(User(count + 1, name, []))
            count += 1
    elif a == '6':
        print("Введите id пользователя")
        id = input()
        remove_user(id)
    elif a == '7':
        print("Введите название книги")
        name = input()
        if not name.isalpha():
            print("Ошибка валидации данных")
        else:
            print("Введите цену книги")
            price = input()
            try:
                if int(price) < 0:
                    print("Ошибка валидации данных")
            except ValueError:
                print("Ошибка валидации данных")
            add_book(Book(count1 + 1, name, price))
            count1 += 1
    elif a == '8':
        print("Введите номер книги")
        id = input()
        remove_book(id)
    elif a == '9':
        print_all_users()
        print_all_books()
    elif a == '11':
        remove_json()
    elif a == '10':
        break
    else:
        print("Ошибка валидации данных")
