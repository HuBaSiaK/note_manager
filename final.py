
username = input("Введите ваше имя ")
first_title = input("Введите первый заголовок ")
second_title = input("Введите второй заголовок ")
third_title = input("Введите третий заголовок ")
titles_list = [first_title,second_title,third_title]
content = input("Введите содержание заметки ")
status = input("Введите текущий статус ")
created_date = input("Введите дату создания в формате: dd-mm-yyyy ")
issue_date = input("Введите дату конца актуальности заметки в формате: dd-mm-yyyy ")


note = [

username,

content,

status,

created_date,

issue_date,

titles_list

]

print(note)