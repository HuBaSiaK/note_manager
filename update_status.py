status = input("Введите статус заметки. Возможные статусы: 'выполнено','в процессе','отложено' ").lower()

#список доступных статусов
allowed_statuses = ['выполнено','в процессе','отложено']

status_changed = False

#цикл пока не добьёмся от пользователя корректного статуса
while status_changed != True:
    #ввод нового статуса
    status_new = input("Введите новый статус заметки. Возможные статусы: 'выполнено','в процессе','отложено' ").lower()
    #проверка корректности ввода
    if allowed_statuses.count(status_new) > 0:
        status = status_new
        status_changed = True
    else:
        print("Вы ввели недопустимый статус. Список доступных статусов:")
        #вывод доступных статусов
        for allowed_status in allowed_statuses:
            print(str(allowed_statuses.index(allowed_status) + 1) + ". " + allowed_status)
dictionary = {"текущий статус" : status}
print("Новый статус заметки: " + dictionary["текущий статус"])
