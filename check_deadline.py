import datetime
current_time = datetime.datetime.now().strftime('%d-%m-%Y')
print(current_time)
issue_date = input("Введите срок выполнения заметки в формате 'dd-mm-yyyy' (например, 12-01-2025): ")
if issue_date < current_time:
    print("Заявка просрочена")