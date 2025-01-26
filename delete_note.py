

def print_notes(notes_list):
    if len(notes_list) == 0:
        print("У вас нет сохранённых заметок!")
    else:
        print("Список заметок:")
        print("------------------------------")
    for note in notes_list:
        print(f"Заявка № {notes_list.index(note) + 1}")
        print(f"Имя пользователя: {note['username']}")
        print(f"Заголовки:")
        for title in note['titles']:
            print(f"{note['titles'].index(title) + 1}. {title}")
        print(f"Содержание: {note['content']}")
        print(f"Статус: {note['status']}")
        print(f"Дата создания: {note['created_date']}")
        print(f"Дата окончания: {note['issue_date']}")
        print("------------------------------")

def print_note(note):
    print("Имя пользователя: ", note["username"])
    for title in note["titles"]:
        print(f"{note["titles"].index(title) + 1}. {title}")
    print("Описание: ", note["content"])
    print("Статус: ", note["status"])
    print("Cоздана: ", note["created_date"][0:5])
    print("Выполнить до: ", note["issue_date"][0:5])


def confirm_deletion():
    confirm_delete = input("Вы уверены, что хотите удалить эту заметка? Введите 'да' для удаления: ").lower() == 'да'
    return confirm_delete

#получим список заметок
from multiple_notes import notes_list
delete_notes = []
#получим от пользователя имя реквизита по которому будем проводить поиск
deletion_type = input("Вы хотите удалить заметку по заголовку или имени создателя? Введите 'заголовок' или 'имя': ")
note_exist = False
#определим ветвь поиска
if deletion_type == 'заголовок':
    title = input("Введите заголовок удаляемой заметки: ")
    for note in notes_list:
        #убедимся, что у данной заметки есть нужный нам ключ
        if 'titles' in note.keys():
            #проверим, что заголовок есть в списке данной заметки
            if title in note["titles"]:
                note_exist = True
                print("Удаляемая заметка:")
                #выведем пользователю заметку перед удалением
                print_note(note)
                #получим подтверждение удаления
                user_confirm = confirm_deletion()
                if user_confirm == True:
                    #добавим заметку в список заметок к удалению
                    delete_notes.append(note)
    if  note_exist == False:
        print(f"Заметок с заголовком '{title}' не найдено!")
elif deletion_type == 'имя':
    username = input("Введите имя пользователя удаляемой заметки: ")
    for note in notes_list:
        if 'username' in note.keys():
            if username == note["username"]:
                note_exist = True
                print("Удаляемая заметка:")
                print_note(note)
                user_confirm = confirm_deletion()
                if user_confirm == True:
                    delete_notes.append(note)
    if  note_exist == False:
        print(f"Заметок с пользователем '{username}' не найдено!")
else:
    print("Неверно введен способ отбора")
for note in delete_notes:
    #удалим заметки из списка к удалению
    notes_list.remove(note)
#выведем пользователю текущий список заметок
print_notes(notes_list)