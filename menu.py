import os
from datetime import datetime
from Note import Note


# -------------- вывод рабочего списка в консоль ------------------------
def printArray(arr):
    for i in range(0, len(arr)):
        outString(arr[i])
        print("i = ", i)


# -------------- сборка строки из рабочего списка для вывода в консоль ------------------------
def outString(n_):
    print(
        "id: ",
        str(n_.id),
        "  ",
        str(n_.date_mark),
        " З",
        str(n_.time_mark),
        " Заголовок: ",
        str(n_.title),
        "  Заметка: ",
        str(n_.body),
    )
    # print("----------------- отпечатались из outString -----------------------")


# -------------- редактирование заметки ------------------------
def editNote(item):
    newTitle = input("Введите новое название заголовка: ")
    newBody = input("Введите новый текст заметки: ")
    item.title = newTitle
    item.body = newBody
    item = rebuildArr(item)
    return item


# -------------- удаление заметки ------------------------
def removeNote(arr, id):
    print("================== зашли в removeNote ==========")
    newArr = []
    for i in range(0, len(arr)):
        if arr[i].id != id:
            print(
                "i = ",
                i,
                "arr[i].id = ",
                arr[i].id,
                "----------- это из  'if arr[i].id != id:' ",
            )
            newArr.append(arr[i])
    printArray(newArr)
    newArr = rebuildArr(newArr)
    print("/////////////////////////////// печать после перестройки в removeNote(): ")
    printArray(newArr)
    return newArr


# -------------- добавление заметки ------------------------
def addNote(arr):
    newTitle = input("Введите заголовок новой заметки: ")
    newBody = input("Введите текст новой заметки: ")
    newDate_mark = (
        str("{:02d}".format(datetime.now().day))
        + "."
        + str("{:02d}".format(datetime.now().month))
        + "."
        + str("{:4d}".format(datetime.now().year))
        + "  "
    )
    newTime_mark = (
        str(datetime.now().hour)
        + ":"
        + str(datetime.now().minute)
        + ":"
        + str(datetime.now().second)
    )
    newNote = Note(Note.units_num, newTitle, newBody, newDate_mark, newTime_mark)
    arr.append(newNote)
    arr = rebuildArr(arr)
    return arr


# -------------- перестроение рабочего списка (коррекция поля Note.id) ------------------------
def rebuildArr(arr):
    workId = 0
    for i in range(0, len(arr)):
        # workId += 1
        arr[i].id = i + 1
    return arr


# -------------- поиск заметки ------------------------------------------------------
# (значения всех полей экземпляра Note собираются в одну строку, далее идет поиск вхождения поискового шаблона в строку)
def findNote(arr):
    findStr = str(
        input("Введите id или любую часть содержимого заметки, несколько символов: ")
    )
    # print("findStr = " + findStr)
    tempStr = ""
    tempArr = []
    for i in range(0, len(arr)):
        tempStr += str(arr[i].id) + " "
        tempStr += arr[i].title + " "
        tempStr += arr[i].body + " "
        tempStr += arr[i].date_mark + " "
        tempStr += arr[i].time_mark + " "

        if findStr.lower() in tempStr.lower():
            tempArr.append(arr[i])
        tempStr = ""

    if len(tempArr) > 0:
        print("Найдено " + str(len(tempArr)) + " похожих записей:")

        for i in range(0, len(tempArr)):
            print(
                "id: ",
                tempArr[i].id,
                " ",
                tempArr[i].title,
                " ",
                tempArr[i].body,
                " ",
                tempArr[i].date_mark,
                " ",
                tempArr[i].time_mark,
                " ",
            )
            # print()
        findId = input("Введите id нужной заметки (цифра в начале строки): ")
        # print("type(findId) = ", type(findId))
        print("Выбрано: ", findId)

        # outString(tempArr[findId])
        out = False
        while out != True:
            print(
                "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
            )
            printArray(arr)
            for i in range(0, len(arr)):
                print("~~~~~~~~~~~~~~~~~~~~~~~~~ ", "len(arr) now is ", len(arr))

                if findId == arr[i].id:
                    print("i = ", i, " findId = ", findId, "  arr[i].id = ", arr[i].id)
                    print(findId == arr[i].id, "---------------------------------")
                    print("Ведите цифру, соответствующую необходимому действию,")
                    print("'1' - Редактировать")
                    print("'2' - Удалить")
                    print("Клавиша 'Enter' - Выйти из редактирования")
                    action = input("Ваш выбор: ")
                    if action == "1":
                        arr[i] = editNote(arr[i])
                        out = True
                    elif action == "2":
                        arr = removeNote(arr, arr[i].id)
                        print(
                            "++++++++++++++++++++++++++++++++    печать после выполнения removeNote"
                        )
                        printArray(arr)
                        print("len(arr) = ", len(arr))
                        out = True
                    elif action == "":
                        out = True
                    else:
                        print("Что-то пошло не так")
                    break
    else:
        print("Похожих записей не найдено")
    pauseIt()
    return arr


# --------------------------- метод приостановки программы ------------------------
def pauseIt():
    str = input("...... press any key, please ...............")


# --------------------------- формирование начального меню ------------------------
def promptMenu():
    print("==================================================")
    print("Выберите пункт меню, нажав соответствующую цифру и Enter.")
    print("1. Найти заметку/Изменить заметку/Удалить заметку")
    print("2. Вывести полный список заметок")
    print("3. Добавить новую заметку")
    print("Q/q - Выйти из программы")


# ======================================================================================================
# Функция главного меню ==================================
# принимает рабочий список, внутри модуля вся работа ведется с ним
def main_Menu(fileContent):
    tempList = list()
    promptMenu()
    getOut = False  # флаг для выхода из меню
    while getOut != True:
        # os.system("CLS")
        printArray(fileContent)

        promptMenu()
        choice = input("Ваш выбор: ")
        choice = choice.lower()
        print(choice)
        if choice == "Q" or choice == "q" or choice == "й" or choice == "Й":
            getOut = True
            print()
            print("Дело хозяйское... До новых встреч!")
            print()
        if choice == "1":
            fileContent = findNote(fileContent)

        if choice == "2":
            printArray(fileContent)

        if choice == "3":
            fileContent = addNote(fileContent)

    return fileContent
