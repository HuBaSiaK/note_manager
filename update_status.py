def update_status(dictionary):

    print(f"Текущий статус заметки:  '{dictionary['текущий статус']}'")

    # список доступных статусов
    allowed_statuses = ['выполнено', 'в процессе', 'отложено']
    status_numbers = ['1', '2', '3']
    status_dict = dict(zip(status_numbers, allowed_statuses))
    # выведем доступные статусы
    print("Выберите новый статус заметки. Доступные статусы:")
    for status_number in status_dict:
        print(f"{status_number}. {status_dict[status_number]}")

    # цикл пока не добьёмся от пользователя корректного статуса
    while True:
        # ввод нового статуса
        status_new = input("Введите имя статуса или его номер: ").lower()
        # проверка корректности ввода
        if status_new in status_dict.values():
            dictionary["текущий статус"] = status_new
            break
        elif status_new in status_dict.keys():
            status_new = status_dict[status_new]
            dictionary["текущий статус"] = status_new
            break
        else:
            print("Вы ввели недопустимый статус. Список доступных статусов:")
            # вывод доступных статусов
            for status_number in status_dict:
                print(f"{status_number}. {status_dict[status_number]}")
    # вывод текущего статуса
    print("Cтатус заметки успешно обновлён на: " + dictionary["текущий статус"])

# получим текущий статус
current_status = input("Введите текущий статус. Доступные статусы 'выполнено', 'в процессе', 'отложено': ")

dictionary = {"текущий статус": current_status}
update_status(dictionary)
