import os


# Cначала наполняем первый список контактами, потом идёт взаимодействие с этими контактами 

def adding(contacts, lastName, firstName, middleName, phoneNumber):
    contacts.append({'lastName': lastName, 'firstName': firstName, 'middleName': middleName, 'phoneNumber': phoneNumber})

def rechange(contacts, lastName, firstName, middleName, phoneNumber):
    for contact in contacts:
        if contact['lastName'].lower() == lastName.lower() and contact['firstName'].lower() == firstName.lower():
            contact['middleName'] = middleName
            contact['phoneNumber'] = phoneNumber

def deleting(contacts, lastName, firstName):
    contacts[:] = [contact for contact in contacts if contact['lastName'].lower() != lastName.lower() or contact['firstName'].lower() != firstName.lower()]

def searching(contacts, key, value):
    results = [contact for contact in contacts if contact[key].lower() == value.lower()]
    return results

def copy(mainContacts, ostContacts, lineNumber):
    if 0 < lineNumber <= len(mainContacts):
        contactForCopy = mainContacts[lineNumber - 1]
        ostContacts.append(contactForCopy)
        print("Контакт скопирован")
    else:
        print("Неверный номер копируемой строки")

def show(contacts):
    if len(contacts) > 0:
        for contact in contacts:
            print(f"{contact['lastName']}, {contact['firstName']}, {contact['middleName']}, {contact['phoneNumber']}")
    else: print(f"Файл не найден или еще не создан")

def detecting(fileSourse):
    contacts = []
    if os.path.exists(fileSourse):
        with open(fileSourse, 'r') as file:
            for line in file:
                data = line.strip().split(',')
                contacts.append({'lastName': data[0], 'firstName': data[1], 'middleName': data[2], 'phoneNumber': data[3]})
    return contacts

def saving(fileSourse, contacts):
    with open(fileSourse, 'w') as file:
        for contact in contacts:
            file.write(f"{contact['lastName']},{contact['firstName']},{contact['middleName']},{contact['phoneNumber']}\n")


def workWithPhonebook():
    originalFile= "phonebook1.txt"
    dublicateFile = "phonebook2.txt"

    mainContacts = detecting(originalFile)
    ostContacts = detecting(dublicateFile)

    while True:
        print("\n1. Добавить контакт")
        print("2. Изменить контакт")
        print("3. Удалить контакт")
        print("4. Поиск контакта из 1-ого списка") 
        print("5. Поиск контакта из 2-ого списка") 
        print("6. Скопировать контакт из 1-ого справочника во 2-ой")
        print("7. Показать контакты из 1-ого справочника")
        print("8. Показать контакты из 2-ого справочника(копия)")
        print("9. Выйти")

        choice = input("Выберите пункт из меню (1/2/3/4/5/6/7/8): ")

        if choice == '1':
            lastName = input("Введите фамилию: ")
            firstName = input("Введите имя: ")
            middleName = input("Введите отчество: ")
            phoneNumber = input("Введите номер телефона: ")
            adding(mainContacts, lastName, firstName, middleName, phoneNumber)
            saving(originalFile, mainContacts)
        elif choice == '2':
            lastName = input("Введите фамилию для изменения: ")
            firstName = input("Введите имя для изменения: ")
            middleName = input("Введите отчество для изменения: ")
            phoneNumber = input("Введите новый номер телефона: ")
            rechange(mainContacts, lastName, firstName, middleName, phoneNumber)
            saving(originalFile, mainContacts)
        elif choice == '3':
            lastName = input("Введите фамилию для удаления: ")
            firstName = input("Введите имя для удаления: ")
            deleting(mainContacts, lastName, firstName)
            saving(originalFile, mainContacts)
        elif choice == '4':
            searchingKey = input("Введите характеристику для поиска (lastName/firstName/middleName/phoneNumber): ")
            searchingValue = input("Введите значение для поиска: ")
            results1 = searching(mainContacts, searchingKey, searchingValue)
            if results1:
                print("\nРезультаты поиска в 1-ом списке:")
                show(results1)
            else:
                print("\nНичего не найдено.")
        elif choice == '5':
            searchingKey = input("Введите характеристику для поиска (lastName/firstName/middleName/phoneNumber): ")
            searchingValue = input("Введите значение для поиска: ")
            results2 = searching(ostContacts, searchingKey, searchingValue)
            if results2:
                print("\nРезультаты поиска во 2-ом списке:")
                show(results2)
            else:
                print("\nНичего не найдено.")
        elif choice == '6':
            lineNumber = int(input("Введите номер копируемой строки из 1-ого списка: "))
            copy(mainContacts, ostContacts, lineNumber)
            saving(dublicateFile, ostContacts)
        elif choice == '7':
            print("\nКонтакты 1-ого списка:")
            show(mainContacts)
        elif choice == '8':
            print("\nКонтакты 2-ого списка:")
            show(ostContacts)
        elif choice == '9':
            break
        else:
            print("Что-то пошло не так... Попробуйте снова")

workWithPhonebook()