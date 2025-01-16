#from final import titles_list

title = 'Тест'
titles_list = []

#цикл для ввода регулируемого пользователем
while title != '' and title.lower() != 'стоп':
    print("Текущий список заголовков:")
    print(titles_list)
    title = input("Введите заголовок заметки. Для остановки ввода сделайте пустой ввод или введите 'стоп'")
    #проверка конца ввода заголовка
    if title != '' and title.lower() != 'стоп':
        title_count = titles_list.count(title)
        #проверим не вводил ли пользователь такой заголвок
        if title_count == 0:
         titles_list.append(title)
        else:
            #сообщим пользователю о наличии такого заголовка в списке
            print("Заголовок '" + title + "' уже добавлен в список")
#выведем пользователю итоговый список
print("Итоговый список заголовков")
for title in titles_list:
    print(str(titles_list.index(title) + 1) + ". " + title)


