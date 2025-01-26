title = 'Тест'
titles_list = []

#цикл для ввода регулируемого пользователем
while title != '' and title.lower() != 'стоп':
    title = input("Введите заголовок заметки. Для остановки оставьте пустой ввод или введите 'стоп': ")
    #проверка конца ввода заголовка
    if title != '' and title.lower() != 'стоп':
        title_count = titles_list.count(title)
        #проверим не вводил ли пользователь такой заголвок
        if title_count == 0:
         titles_list.append(title)
        else:
            #сообщим пользователю о наличии такого заголовка в списке
            print("Заголовок '" + title + "' уже добавлен в список. Попробуйте другой")
#выведем пользователю итоговый список
if len(titles_list) == 0:
    print("Вы не ввели заголовки для заметки!")
else:
    print("Итоговый список заголовков заметки:")
    for title in titles_list:
        print(str(titles_list.index(title) + 1) + ". " + title)


