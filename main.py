# Реализовать консольное приложение заметки, с сохранением, чтением,
# добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.

import functions as f

def procCommand(cmd):
    if cmd == 0:
        f.save(phones)
        return False
    elif cmd in range(1, 4):
        rezFind = f.findContacts(phones, cmd)
        print ('Найденные контакты:')
        for zap in rezFind:
            print(*f.printContacts(phones, phones.index(zap) + 1))
    elif cmd == 4:
        f.addContact(phones)
    elif cmd == 5:
        print("\n".join(f.printContacts(phones)))
        f.editContact(phones)
    elif cmd == 6:
        print("\n".join(f.printContacts(phones)))
        f.delContact(phones)
    elif cmd == 7:
        print("\n".join(f.printContacts(phones)))
    else:
        print ('Неизвестна команда')
    return True

phones = f.load()
print(f.printHelp())

while True:
    try:
        inputCommand = int(input('Введите номер команды: '))
        if not procCommand(inputCommand):
            break
    except ValueError:
        print('Неизвестная')