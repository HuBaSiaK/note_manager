def get_digits(number):
    new_number = number
    digit_list = []
    #digit_number = 1
    #while 10**digit_list <= new_number:
    while 1 <= new_number:
        digit_list.append(new_number % 10)
        new_number = new_number // 10
    digit_list.reverse()
    return digit_list
# number = int(input("Введите трёхзначное число: "))
# hundreds = (number % 1000) // 100
# print(f"В вашем числе {hundreds} сотен")
# thousands = (number % 10000) // 1000
# print(f"В вашем числе {thousands} тысяч")

#Функция ввода даты пользователем
def user_date_input():
    import datetime
    while True:
        issue_date = input("Введите срок выполнения заметки в формате 'dd-mm-yyyy' (например, 12-01-2025): ")
        # приводим строку введённую пользователем к дате
        try:
            # приводим строку введённую пользователем к дате
            issue_date = datetime.datetime.strptime(issue_date, '%d-%m-%Y')
            break
        except:
            print("Некорректный формат даты. Попробуйте снова.")
    return issue_date.date()

#вычисление разницы дней между двумя датами
def day_difference(date_1, date_2):
    return (date_1 - date_2).days

#получаем текущую дату
def get_today():
    import datetime
    return datetime.datetime.now().date()

import datetime
#получаем текущую дату
current_time = get_today()
#получаем строковое представление текущей даты
current_time_str = current_time.strftime('%d-%m-%Y')
print(f"Текущая дата: {current_time_str}")
issue_date = user_date_input()
#проверяем истекла ли заметка
num_days = day_difference(issue_date, current_time)
if num_days == 0:
    print("Дедлайн сегодня!")
elif num_days < 0:
    print(f"Дедлайн истёк {-num_days} дней назад")
else:
    print(f"До истечения срока заметки осталось дней {str(num_days)}")