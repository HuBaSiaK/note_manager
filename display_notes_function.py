def display_notes(notes):
    if len(notes) == 0:
        print("У вас нет сохранённых заметок!")
    else:
        print("Список заметок:")
        print("------------------------------")
    for note in notes:
        print(f"Заявка № {notes.index(note) + 1}")
        print(f"Имя пользователя: {note['username']}")
        print(f"Заголовки:")
        for title in note['titles']:
            print(f"{note['titles'].index(title) + 1}. {title}")
        print(f"Содержание: {note['content']}")
        print(f"Статус: {note['status']}")
        print(f"Дата создания: {note['created_date']}")
        print(f"Дата окончания: {note['issue_date']}")
        print("------------------------------")

def create_note():
    from datetime import datetime
    username = input("Введите ваше имя: ")
    title = 'Тест'
    titles_list = []

    # цикл для ввода регулируемого пользователем
    while title != '' and title.lower() != 'стоп':
        print("Текущий список заголовков:")
        print(titles_list)
        title = input("Введите заголовок заметки. Для остановки ввода сделайте пустой ввод или введите 'стоп'")
        # проверка конца ввода заголовка
        if title != '' and title.lower() != 'стоп':
            title_count = titles_list.count(title)
            # проверим не вводил ли пользователь такой заголвок
            if title_count == 0:
                titles_list.append(title)
            else:
                # сообщим пользователю о наличии такого заголовка в списке
                print("Заголовок '" + title + "' уже добавлен в список")
    content = input("Введите содержание заметки ")
    status = input("Введите текущий статус ")
    created_date = datetime.now().strftime('%d-%m-%Y')
    its_date = False
    while not its_date == True:
        issue_date = input("Введите срок выполнения заметки в формате 'dd-mm-yyyy': ")
        its_date = check_date(issue_date)
        if its_date == False:
            print("Ваш ввод не соответствует формату или не является датой")
    note = {"username" : username, "titles" : titles_list, "content" : content, "status" : status,
          "created_date" : created_date, "issue_date" : issue_date}
    return note

def check_date(date_):
    from datetime import datetime
    try:
        datetime.strptime(date_, '%d-%m-%Y')
        return True
    except Exception:
        return False

note = create_note()
notes = []
notes.append(note)
display_notes(notes)
