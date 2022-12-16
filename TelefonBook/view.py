import funk as f


def menu():
    print('Здравствуйте!\nВас приветствует самая лучшая телефонная книга')
    variant = input('Вы можете: \nДобавить контакт - нажмите 1;\
         \nУдалить контакт - нажмите 2;\
         \nИсправить контакт - нажмите 3;\
          \nПоиск заветного контакта - нажмите 4;\
           \nИмпорт телефонной книги из файла - нажмите 5;\
           \nВыйти из книги - 0;\
            \nВведите пункт меню - ')
    return variant


def print_adding_contact():
    surname = input("Введите фамилию: ")
    first_name = input("Введите имя: ")
    patronymic = input("Введите отчество: ")
    phone_number = input("Введите номер телефона: ")
    f.add_contact(surname, first_name, patronymic, phone_number)
    print("Контакт сохранен")


def print_search():
    word = input("Введите данные для поиска: ")
    data = f.export_data()
    item = f.search_data(word, data)
    if item != None:
        print("Фамилия".center(20), "Имя".center(20),
              "Телефон".center(15), "Примечание".center(30))
        print("-"*85)
        print(item)
    else:
        print("Данные не обнаружены")


def print_import_book(name_file):
    print(f"Контакты из файла {name_file} добавлены!")


def print_exit():
    print("До новых встреч!")
