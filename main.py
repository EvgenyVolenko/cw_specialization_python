# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.

# Критерии оценки
# Приложение должно запускаться без ошибок, должно уметь сохранять данные
# в файл, уметь читать данные из файла, делать выборку по дате, выводить на
# экран выбранную запись, выводить на экран весь список записок, добавлять
# записку, редактировать ее и удалять.

import functions as f

def procCommand(cmd):
    if cmd == 0:
        f.save(notes)
        return False
    elif cmd == 6:
        rezFind = f.findNotes(notes, cmd)
        print ('Найденные записки:')
        for zap in rezFind:
            print(*f.printNotes(notes, notes.index(zap) + 1))
    elif cmd == 1:
        f.addNote(notes)
    elif cmd == 2:
        print("\n".join(f.printNotes(notes)))
        f.editNote(notes)
    elif cmd == 3:
        print("\n".join(f.printNotes(notes)))
        f.delNote(notes)
    elif cmd == 4:
        print("\n".join(f.printNotes(notes)))
        f.printOneNote(notes)
    elif cmd == 5:
        print("\n".join(f.printNotes(notes)))
    else:
        print ('Неизвестна команда')
    return True

notes = f.load()
print(f.printHelp())

while True:
    try:
        inputCommand = int(input('Введите номер команды: '))
        if not procCommand(inputCommand):
            break
    except ValueError:
        print('Вы ввели неизвестную команду')