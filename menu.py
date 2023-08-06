# from main_notes import *
import os
from datetime import datetime

# from main_notes import *

from Note import Note


def printArray(arr):
    for i in range(0, len(arr)):
        outString(arr[i])
        print()


def outString(n_):
    print(
        "id:"
        + str(n_.id)
        + " "
        + str(n_.date_mark)
        + " "
        + str(n_.time_mark)
        + " Заголовок: "
        + str(n_.title)
        + "  Заметка: "
        + str(n_.body)
    )
    # print(str(n_.title) + str(n_.body))


def editNote(item):
    newTitle = input("Введите новое название заголовка: ")
    newBody = input("Введите новый текст заметки: ")
    item.title = newTitle
    item.body = newBody
    item = rebuildArr(item)
    return item


def removeNote(arr, id):
    newArr = []
    for i in range(0, len(arr)):
        if arr[i].id != id:
            newArr.append(arr[i])
            newArr = rebuildArr(newArr)
    return newArr


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


def rebuildArr(arr):
    workId = 0
    for i in range(0, len(arr)):
        workId += 1
        arr[i].id = workId
    return arr


def findNote(arr):
    findStr = input(
        "Введите id или любую часть содержимого заметки, несколько символов: "
    )
    # print(findStr)
    tempStr = ""
    tempArr = []
    # print(type(arr))
    for i in range(0, len(arr)):
        tempStr += str(arr[i].id) + " "
        tempStr += arr[i].title + " "
        tempStr += arr[i].body + " "
        tempStr += arr[i].date_mark + " "
        tempStr += arr[i].time_mark + " "
        # print(arr[i])
        # print(
        #     "findStr.lower() = "
        #     + findStr.lower()
        #     + "  tempStr.lower() = "
        #     + tempStr.lower()
        # )
        if findStr.lower() in tempStr.lower():
            tempArr.append(arr[i])
        tempStr = ""
    if len(tempArr) > 0:
        print("Найдено " + str(len(tempArr)) + " похожих записей:")

        for i in range(0, len(tempArr)):
            print(
                "id: "
                + tempArr[i].id
                + " "
                + " "
                + tempArr[i].title
                + " "
                + tempArr[i].body
                + " "
                + tempArr[i].date_mark
                + " "
                + tempArr[i].time_mark
                + " "
            )
            print()
        findId = input("Введите id нужной заметки (цифра в начале строки): ")
        print("Выбрано: ")
        outString(tempArr[i])
        out = False
        while out != True:
            print()
            for i in range(0, len(arr)):
                if findId == arr[i].id:
                    print("Ведите цифру, соответствующую необходимому действию,")
                    print("'1' - Редактировать")
                    print("'2' - Удалить")
                    print("Клавиша 'Enter' - Выйти из редактирования")
                    # print("Q/q. ")
                    action = input("Ваш выбор: ")
                    if action == "1":
                        arr[i] = editNote(arr[i])
                        out = True
                    elif action == "2":
                        arr = removeNote(arr, arr[i].id)
                        printArray(arr)
                        out = True
                        # print("Нет пока такой функции, но мы работаем над этим")
                    elif action == "":
                        out = True
                    else:
                        print("Что-то пошло не так")
    else:
        print("Похожих записей не найдено")
    pauseIt()
    return arr


def pauseIt():
    # choice = input("Ваш выбор: ")
    str = input("...... press any key, please ...............")


def promptMenu():
    print("==================================================")
    print("Выберите пункт меню, нажав соответствующую цифру и Enter.")
    print("1. Найти заметку/Изменить заметку/Удалить заметку")
    print("2. Вывести полный список заметок")
    print("3. Добавить новую заметку")
    print("Q/q - Выйти из программы")
    # return strPr


# Функция главного меню ==================================
def main_Menu(fileContent):
    print("================ вошли в главное меню ======================")
    tempList = list()
    promptMenu()
    # print(prompt())
    getOut = False  # флаг для выхода из меню
    while getOut != True:
        # os.system("CLS")
        # printArray(fileContent)

        promptMenu()
        choice = input("Ваш выбор: ")
        choice = choice.lower()
        print(choice)
        # pauseIt()
        if choice == "Q" or choice == "q" or choice == "й" or choice == "Й":
            getOut = True
            # saveFile(fileContent, "phones.txt")
            print()
            print("Дело хозяйское... До новых встреч!")
            print()
        if choice == "1":
            fileContent = findNote(fileContent)

        if choice == "2":
            printArray(fileContent)

        if choice == "3":
            fileContent = addNote(fileContent)

        # if choice == "4":
        # saveFile(fileContent, "phones.txt")

        # print(choice)

    return fileContent
