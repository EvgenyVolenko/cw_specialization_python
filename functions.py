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

def findNotes(notes):
    text = input('Введите дату заметки в формате ДД.ММ.ГГГГ: ')
    
    result = []
    for note in notes:
        if note['dataNote'] == text:
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
                result += str(value) + ' '
            rezret.append(result)
            num += 1
    else: 
        result = ''
        note = notes[numberN - 1]
        for value in note.values():
            result += str(value) + ' '
        rezret.append(result)
    return rezret

def printOneNote(notes):
    printNotes(notes)
    try:
        numberShow = int(input('Введите номер записи для вывода на экран: '))
        note = notes[numberShow - 1]
        print("\nВремя заметки: %s" %note["timeNote"])
        print("Дата заметки: %s" %note["dataNote"])
        print("Заголовок заметки: %s" %note["header"])
        print("Текст заметки: %s" %note["body"])
    except:
        print('Введен недопустимый параметр!')

def addNote(notes):
    print('Введите данные новой заметки: ')
    note = {}
    note["header"] = input("Введите заголовок заметки: ")
    note["body"] = input("Введите текст заметки: ")
    today = datetime.datetime.today()
    note["dataNote"] = today.strftime("%m.%d.%Y")
    note["timeNote"] = today.strftime("%H:%M:%S")
    notes.append(note)

def delNote(notes):
    printNotes(notes)
    try:
        numberDel = int(input('Введите номер записи для удаления из справочника: '))
        del notes[numberDel - 1]
    except:
        print('Введен недопустимый параметр!')

def editNote(notes):
    try:
        numberEdit = int(input('Введите номер записи для редактирования: '))
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
    