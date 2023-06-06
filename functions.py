import json
from easygui import *

fileName = 'notebook.json'

def load():
    with open(fileName,"r",encoding="utf-8") as fh:
        return json.load(fh)
    
def save(phones):
    with open(fileName, 'w', encoding='utf-8') as fh:
        fh.write(json.dumps(phones, ensure_ascii = False))
    print('Заметки успешно coxpanenы в файле %s' %fileName)

def printHelp():
    strHelp = '''\nКоманды заметок:
    1 - Добавить заметку
    2 - Редактировать заметку по номеру записи
    3 - Удалить заметку по номеру записи
    4 - Показать заметку по номеру записи
    4 - Показать список заметок
    5 - Поиск по дате
    0 - ВЫХОД'''
    return strHelp

def isPhoneExist(phones, phoneFind):
    for phone in phones:
        for value in phone.values():
            if phoneFind in value:
                return True
    return False

def findContacts(phones, cmd):
    strHelp = 'Введите '
    if cmd == 1:
        strHelp += 'имя контакта: '
    elif cmd == 2:
        strHelp += 'фамилию контакта: '
    else:
        strHelp += 'номер телефона: '
    text = input(strHelp).upper()

    result = []
    for contact in phones:
        isExists = False
        for key, value in contact.items():
            if key != 'phones' and text in value.upper():
                if cmd == 1 and key == 'firstName' or cmd == 2 and key == 'lastName':
                    isExists = True
            
            if not isExists and cmd not in range(1, 3) and key == 'phones':
                isExists = isPhoneExist(contact['phones'], text)

        if isExists:
            result.append(contact)

    return result

def printContacts(phones, numberC = 0):
    num = 1
    rezret = []
    if numberC == 0:
        for contact in phones:
            result = ''
            result += str(num) + " "
            for value in contact.values():
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
        contact = phones[numberC - 1]
        for value in contact.values():
            if type(value) is list:
                for znach in value:
                    for value1 in znach.values():
                        result += str(value1) + ' '
            else:
                result += str(value) + ' '
        rezret.append(result)
    return rezret

def addContact(phones):
    # {"lastName": "Иванов", "firstName": "Иван", "surName": "Иванович", "phones": [{"title": "Основной", "number": "79011234567"}, {"title": "Домашний", "number": "79991234567"}]} 
    print('Введите данные нового контакта: ')
    human = {}
    human["lastName"] = input("Введите фамилию ")
    human["firstName"] = input("Введите имя ")
    human["sureName"] = input("Введите отчество ")
    print ('Введите телефоны контакта ')
    phonesH = []
    
    while True:
        phoneZapis = {}
        typePhone = input("Введите тип номера телефона ")
        phoneN = input("Введите номер телефона ")
        if phoneN == '':
            break
        else:
            phoneZapis["title"] = typePhone
            phoneZapis["number"] = phoneN
            phonesH.append(phoneZapis)
    
    human["phones"] = phonesH

    phones.append(human)

def delContact(phones):
    printContacts(phones)
    try:
        numberDel = int(input('Введите номер записи для удаления из справочника '))
        del phones[numberDel - 1]
    except:
        print('Введен недопустимый параметр!')

def editContact(phones):
    try:
        numberEdit = int(input('Введите номер записи для редактирования '))
        human = phones[numberEdit - 1]
        printContacts(phones, numberEdit)
        lastName = input("Введите новую фамилию. Если менять не нужно нажмите 'Enter' ")
        if lastName == '':
            print ("Фамилия без изменений")
        else:
            human["lastName"] = lastName

        firstName = input("Введите новое имя. Если менять не нужно нажмите 'Enter' ")
        if firstName == '':
            print ("Имя без изменений")
        else:
            human["firstName"] = firstName

        sureName = input("Введите новое отчество. Если менять не нужно нажмите 'Enter' ")
        if sureName == '':
            print ("Отчество без изменений")
        else:
            human["sureName"] = sureName
                
        for phoneZapis in human["phones"]:
            print(phoneZapis['title'], phoneZapis['number'])
            typePhone = input("Введите тип номера телефона. Если менять не нужно нажмите 'Enter' ")
            if typePhone == '':
                print ("Тип номера без изменений")
            else:
                phoneZapis["title"] = typePhone

            phoneN = input("Введите номер телефона. Если менять не нужно нажмите 'Enter' ")
            if phoneN == '':
                print ("Номер без изменений")
            else:
                phoneZapis["number"] = phoneN
                
    except:
        print('Введен недопустимый параметр!')

# def vvod():
#     msg = printHelp()
#     title = "Выбор команды" #Шапочка.
#     return integerbox(msg, title, default=None, lowerbound=0, upperbound=7, image=None, root=None)
    