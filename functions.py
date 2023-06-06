import json
import datetime
from easygui import *

fileName = "notebook.json"

def load():
    with open(fileName,"r",encoding="utf-8") as fh:
        text = json.loads(fh.read())
        return text
    
def save(notes):
    with open(fileName, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(notes, ensure_ascii = False))
    print('Заметки успешно coxpanenы в файле %s' %fileName)

def printHelp():
    strHelp = '''\nКоманды заметок:
    1 - Добавить заметку
    2 - Редактировать заметку по номеру записи
    3 - Удалить заметку по номеру записи
    4 - Показать заметку по номеру записи
    5 - Показать список заметок
    6 - Поиск по дате
    0 - ВЫХОД'''
    return strHelp

def isNoteExist(notes, noteFind):
    for note in notes:
        for value in note.values():
            if noteFind in value:
                return True
    return False

def findNotes(notes, cmd):
    strHelp = 'Введите '
    if cmd == 6:
        strHelp += 'дату заметки: '
    text = input(strHelp).upper()

    result = []
    for note in notes:
        isExists = False
        for key, value in note.items():
            if key != 'notes' and text in value.upper():
                if cmd == 6 and key == 'dataNote':
                    isExists = True
            
            if not isExists and cmd not in range(1, 3) and key == 'notes':
                isExists = isNoteExist(note['notes'], text)

        if isExists:
            result.append(note)

    return result

def printNotes(notes, numberN = 0):
    num = 1
    rezret = []
    if numberN == 0:
        for note in notes:
            result = ''
            result += str(num) + " "
            for value in note.values():
                if type(value) is list:
                    for znach in value:
                        for value1 in znach.values():
                            result += str(value1) + ' '
                else:
                    result += str(value) + ' '
            rezret.append(result)
            num += 1
    else: 
        result = ''
        note = notes[numberN - 1]
        for value in note.values():
            if type(value) is list:
                for znach in value:
                    for value1 in znach.values():
                        result += str(value1) + ' '
            else:
                result += str(value) + ' '
        rezret.append(result)
    return rezret

def addNote(notes):
    print('Введите данные новой заметки: ')
    note = {}
    note["header"] = input("Введите заголовок заметки ")
    note["body"] = input("Введите текст заметки ")
    today = datetime.datetime.today()
    note["dataNote"] = today.strftime("%m.%d.%Y")
    note["timeNote"] = today.strftime("%H:%M:%S")
    print(note)
    notes.append(note)

def delNote(notes):
    printNotes(notes)
    try:
        numberDel = int(input('Введите номер записи для удаления из справочника '))
        del notes[numberDel - 1]
    except:
        print('Введен недопустимый параметр!')

def editNote(notes):
    try:
        numberEdit = int(input('Введите номер записи для редактирования '))
        note = notes[numberEdit - 1]
        printNotes(notes, numberEdit)
        header = input("Введите новый загловок. Если менять не нужно нажмите 'Enter' ")
        if header == '':
            print ("Заголовок без изменений")
        else:
            note["header"] = header

        body = input("Введите новый текст. Если менять не нужно нажмите 'Enter' ")
        if body == '':
            print ("Текст без изменений")
        else:
            note["body"] = body

        today = datetime.datetime.today()
        note["dataNote"] = today.strftime("%m.%d.%Y")
        note["timeNote"] = today.strftime("%H:%M:%S")
                
    except:
        print('Введен недопустимый параметр!')
    