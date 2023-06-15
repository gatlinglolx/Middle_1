import operations
import Notes
import ui

number = 6  # Кол-во минимально допустимых знаков


def add():
    note = ui.create_note(number)
    array = operations.read_file()
    for notes in array:
        if Notes.Note.get_id(note) == Notes.Note.get_id(notes):
            Notes.Note.set_id(note)
    array.append(note)
    operations.write_file(array, 'a')
    print('Заметка успешно добавлена!')


def show(text):
    logic = True
    array = operations.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Notes.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Notes.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Notes.Note.get_date(notes):
                print(Notes.Note.map_note(notes))
    if logic == True:
        print('Ошибка! Нет ни одной заметки')


def id_edit_del_show(text):
    id = input('Введите id заметки: ')
    array = operations.read_file()
    logic = True
    for notes in array:
        if id == Notes.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Notes.Note.set_title(notes, note.get_title())
                Notes.Note.set_body(notes, note.get_body())
                Notes.Note.set_date(notes)
                print('Заметка успешно изменена!')
            if text == 'del':
                array.remove(notes)
                print('Заметка успешно удалена!')
            if text == 'show':
                print(Notes.Note.map_note(notes))
    if logic == True:
        print('Ошибка! Неверный id')
    operations.write_file(array, 'a')