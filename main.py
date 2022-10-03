from Manager import *
from model.User import User
from model.Book import Book
from exception.UpdatingExistingObjectException import UpdatingExistingObjectException
from exception.InvalidNameException import InvalidNameException

count = 0
count1 = 0
print_menu()
while True:
    a = input()
    if a == '1':
        print("Введите путь к файлу,где будут хранится пользователи")
        a = input()
        save_json(a)
        print("Введите путь к файлу,где будут хранится книги")
        b = input()
        save_xml(b)
    elif a == '2':
        try:
            print("Введите путь к файлу,где хранятся пользователи")
            a = input()
            count = load_json(a).__len__()
        except AttributeError:
            print("\n")
        print("Введите путь к файлу,где хранятся книги")
        b = input()
        load_xml(b)

    elif a == '3':
        print("Введите id пользователя")
        try:
            user = input()
            int(user)
            if not is_user_exist(int(user)):
                raise NonFindException("Нет обьекта с id: " + str(user))
        except ValueError:
            print("Значение некорректно")
            continue
        except NonFindException as e:
            print(e)
            continue
        print("Введите id книги")
        try:
            id = input()
            int(id)
            if not is_user_exist(int(id)):
                raise NonFindException("Нет обьекта с id: " + str(id))
        except ValueError:
            print("Значение некорректно")
            continue
        except NonFindException as e:
            print(e)
            continue
        add_book_to_user(int(user), int(id))
    elif a == '4':
        print("Введите id пользователя")
        try:
            user = input()
            int(user)
            if not is_user_exist(int(user)):
                raise NonFindException("Нет обьекта с id: " + str(user))
        except ValueError:
            print("Значение некорректно")
            continue
        except NonFindException as e:
            print(e)
            continue
        print("Введите id книги")
        try:
            id = input()
            int(id)
            if not is_user_exist(int(id)):
                raise NonFindException("Нет обьекта с id: " + str(id))
        except ValueError:
            print("Значение некорректно")
            continue
        except NonFindException as e:
            print(e)
            continue
        remove_book_to_user(int(user), int(id))
    elif a == '5':
        print("Введите имя пользователя")
        name = input()
        try:
            if not name.isalpha():
                raise InvalidNameException("Имя может состоять только из букв")
        except InvalidNameException as e:
            print(e)
            continue
        add_user(User(count + 1, name, []))
        count += 1
    elif a == '6':
        print("Введите id пользователя")
        try:
            id = input()
            int(id)
            if not is_user_exist(int(id)):
                raise NonFindException("Нет обьекта с id: "+id)
        except NonFindException as e:
            print(e)
            continue
        except ValueError as e:
            print("Некорректные данные")
            continue
        remove_user(id)
    elif a == '7':
        print("Введите название книги")
        name = input()
        try:
            if not name:
                raise InvalidNameException("Имя не может быть пустым")
        except InvalidNameException as e:
            print(e)
            continue
        else:
            print("Введите цену книги")
            price = input()
            try:
                if int(price) < 0:
                    raise ValueError("Цена не может быть меньше 0")
            except ValueError:
                print("Ценой может быть только число!")
            add_book(Book(count1 + 1, name, price))
            count1 += 1
    elif a == '8':
        print("Введите id пользователя")
        try:
            id = input()
            int(id)
            if not is_book_exist(int(id)):
                raise NonFindException("Нет обьекта с id: " + id)
        except NonFindException as e:
            print(e)
            continue
        except ValueError as e:
            print("Некорректные данные")
            continue
        remove_book(id)
    elif a == '9':
        print_all_users()
        print_all_books()
    elif a == '11':
        remove_json()
    elif a == '10':
        break
    elif a == '12':
        print("Введите id пользователя")
        try:
            id=input()
            int(id)
            if not is_user_exist(int(id)):
                raise UpdatingExistingObjectException("Попытка обновить несуществующий оъект")
        except ValueError as e:
            print("Значение некорректно")
            continue
        except UpdatingExistingObjectException as x:
            print(x)
            continue
        print("Введите новое имя пользователя")
        name = input()
        try:
            if not name.isalpha():
                raise InvalidNameException("Имя может содержать только буквы")
        except InvalidNameException as e:
            print(e)
            continue
        update_user(int(id), User(int(id), name, []))
    elif a == '13':
        print("Введите id книги")
        try:
            id = input()
            int(id)
            if not is_book_exist(int(id)):
                raise UpdatingExistingObjectException("Попытка обновить несуществующий оъект")
        except ValueError as e:
            print("Значение некорректно")
            continue
        except UpdatingExistingObjectException as x:
            print(x)
            continue
        print("Введите новое название книги")
        name = input()
        try:
            if not name:
                raise InvalidNameException("Название не может быть пустым")
        except InvalidNameException as e:
            print(e)
            continue
        print("Введите новую цену книги")
        price = input()
        try:
            int(price)
            if int(price) < 0:
                raise ValueError("Цена не может быть меньше нуля или содержать символы кроме цифр")
        except ValueError as e:
            print(e)
            continue
        update_book(int(id), Book(int(id), name, int(price)))
    else:
        print("Не правильно введена команда")
