created_date = input("Введите дату создания заметки в формате 'dd-mm-yyyy' (например, 12-01-2025): ")
#created_date = "11-01-2025"
temp_created_date = created_date[0:5]
print(temp_created_date)
issue_date = input("Введите срок выполнения заметки в формате 'день месяц год' (например, 15 января 2025): ")
#issue_date = "15 апреля 2025"
dateparts = issue_date.split()
dateparts.pop(2)
print(" ".join(dateparts))