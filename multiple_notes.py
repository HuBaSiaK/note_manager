
def print_notes(notes_list):
    print("Список заметок:")
    for note in notes_list:
        print(f"Заметка № {notes_list.index(note) + 1}")
        print("Имя пользователя: ", note["username"])
        for title in note["titles"]:
            print(f"{note["titles"].index(title) + 1}. {title}")
        print("Описание: ", note["content"])
        print("Статус: ", note["status"])
        print("Cоздана: ", note["created_date"][0:5])
        print("Выполнить до: ", note["issue_date"][0:5])

def delete_note_from_list(notes_list, note_index):
    notes_list.remove(notes_list[note_index])

def its_number(number):
    try:
        int(number)
        return True
    except:
        return False

#Функция ввода даты пользователем
def user_date_input():
    import datetime
    while True:
        issue_date = input("Введите срок выполнения заметки в формате 'dd-mm-yyyy' (например, 12-01-2025): ")
        # проверяем, что дата соотвествует формату и является датой
        try:
            datetime.datetime.strptime(issue_date, '%d-%m-%Y')
            break
        except:
            print("Некорректный формат даты. Попробуйте снова.")
    return issue_date

def create_note():
    from datetime import datetime
    username = input("Введите ваше имя: ")
    title = 'Тест'
    titles_list = []

    # цикл для ввода регулируемого пользователем
    while title != '' and title.lower() != 'стоп':
        #print("Текущий список заголовков:")
        #print(titles_list)
        title = input("Введите заголовок заметки. Для остановки ввода сделайте пустой ввод или введите 'стоп': ")
        # проверка конца ввода заголовка
        if title != '' and title.lower() != 'стоп':
            title_count = titles_list.count(title)
            # проверим не вводил ли пользователь такой заголвок
            if title_count == 0:
                titles_list.append(title)
            else:
                # сообщим пользователю о наличии такого заголовка в списке
                print("Заголовок '" + title + "' уже добавлен в список")
    content = input("Введите содержание заметки: ")
    status = input("Введите текущий статус: ")
    created_date = datetime.now().strftime('%d-%m-%Y')
    issue_date = user_date_input()
    note = {"username" : username, "titles" : titles_list, "content" : content, "status" : status,
          "created_date" : created_date, "issue_date" : issue_date}
    return note


print("Добро пожаловать в 'Менеджер заметок'! Вы можете добавить новую заметку.")
notes_list = []
while True:
    note = create_note()
    notes_list.append(note)
    input_over = input("Продолжить ввод заметок? Для остановки введите 'стоп': ").lower() == 'стоп'
    if input_over == True:
        break
print_notes(notes_list)
delete_note = input("Хотите удалить заметку по номеру? Для удаления введите 'да': ").lower() == "да"
if delete_note == True:
    while True:
        note_number = input("Введите номер заметки: ")
        if its_number(note_number):
            note_number = int(note_number)
            if note_number - 1 in range(len(notes_list)):
                delete_note_from_list(notes_list, note_number - 1)
                break
            else:
                print("Заявки с таким номером нет в списке!")
        else:
            print("Вы ввели не номер!")
    print_notes(notes_list)

