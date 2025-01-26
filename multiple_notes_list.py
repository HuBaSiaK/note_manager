
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


input_over = False
notes_list = []

while input_over == False:
    input_over = input("Продолжить ввод заметок? Для остановки введите 'стоп'").lower() == 'стоп'
    if input_over == False:
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
        # выведем пользователю итоговый список
        print("Итоговый список заголовков")
        for title in titles_list:
            print(str(titles_list.index(title) + 1) + ". " + title)

        #from add_titles_loop import titles_list
        #first_title = input("Введите первый заголовок: ")
        #second_title = input("Введите второй заголовок: ")
        # #third_title = input("Введите третий заголовок: ")
        # #titles_list = [first_title,second_title,third_title]
        # titles_list.append(input("Введите первый заголовок: "))
        # titles_list.append(input("Введите второй заголовок: "))
        # titles_list.append(input("Введите третий заголовок: "))
        content = input("Введите содержание заметки: ")
        status = input("Введите текущий статус: ")
        created_date = input("Введите дату создания в формате 'dd-mm-yyyy' (например, 12-01-2025): ")
        issue_date = input("Введите срок выполнения заметки в формате 'dd-mm-yyyy' (например, 12-01-2025): ")
        note = []
        note.append(username)
        note.append(content)
        note.append(status)
        note.append(created_date)
        note.append(issue_date)
        note.append(titles_list)
        notes_list.append(note)

for note in notes_list:
    print("Заметка:", notes_list.index(note)+1)
    print("Имя пользователя: ", note[0])
    for title in note[5]:
            print(str(note[5].index(title) + 1) + ". " + title)
    print("Описание: ", note[1])
    print("Статус: ", note[2])
    print("Cоздана: ", note[3][0:5])
    print("Выполнить до: ", note[4][0:5])