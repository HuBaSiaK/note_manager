username = input("Введите ваше имя: ")
#title = input("Введите заголовок заметки ")
titles_list = []
titles_list.append(input("Введите первый заголовок: "))
titles_list.append(input("Введите второй заголовок: "))
titles_list.append(input("Введите третий заголовок: "))
#titles_list = [first_title,second_title,third_title]
content = input("Введите содержание заметки ")
status = input("Введите текущий статус ")
created_date = input("Введите дату создания в формате 'dd-mm-yyyy': ")
issue_date = input("Введите срок выполнения заметки в формате 'dd-mm-yyyy': ")

print("Заметка:")
print("Имя пользователя: ", username)
print("Заголовок: ", titles_list[0])
print("Подзаголовки: " + titles_list[1] + ", " + titles_list[2])
print("Описание: ", content)
print("Статус: ", status)
print("Cоздана: ", created_date[0:5])
print("Выполнить до: ", issue_date[0:5])