
username = input("Введите ваше имя: ")
first_title = input("Введите первый заголовок: ")
second_title = input("Введите второй заголовок: ")
third_title = input("Введите третий заголовок: ")
titles_list = [first_title,second_title,third_title]
content = input("Введите содержание заметки: ")
status = input("Введите текущий статус: ")
created_date = input("Введите дату создания в формате 'dd-mm-yyyy' (например, 12-01-2025): ")
issue_date = input("Введите срок выполнения заметки в формате 'dd-mm-yyyy' (например, 12-01-2025): ")

note = [
username,
content,
status,
created_date,
issue_date,  
titles_list
]

print("Заметка:")
print("Имя пользователя: ", note[0])
print("Заголовок: ", note[5][0])
print("Подзаголовки: " + note[5][1] + ", " + note[5][2])
print("Описание: ", note[1])
print("Статус: ", note[2])
print("Cоздана: ", note[3][0:5])
print("Выполнить до: ", note[4][0:5])