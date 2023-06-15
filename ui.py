import Notes


def create_note(number):
    title = check_len_text_input(
        input('Введите название заметки: '), number)
    body = check_len_text_input(
        input('Введите текст: '), number)
    return Notes.Note(title=title, body=body)


def menu():
    print("\nПрограмма 'Заметки'\n\nДоступны следующие операции:\n\n1 - Показать все заметки\n2 - Добавить заметку\n3 - Удалить заметку\n4 - Редактировать заметку\n5 - Выборка по дате\n6 - Показать заметку по id\nq - выход\n\nВыберите операцию: ")


def check_len_text_input(text, n):
    while len(text) <= n:
        print(f'Текст должен быть больше {n} символов\n')
        text = input('Введите текст: ')
    else:
        return text


def goodbuy():
    print("До свидания")