from datetime import datetime

# from menu import main_Menu

from menu import main_Menu
from Note import *
from dump import *
import os


# def outString(n_):
#     print(
#         "id:"
#         + str(n_.id)
#         + " "
#         + str(n_.date_mark)
#         + " "
#         + str(n_.time_mark)
#         + "  "
#         + str(n_.title)
#         + "  "
#         + str(n_.body)
#     )
# print(str(n_.title) + str(n_.body))


def makeArray(count):
    arr = []
    for i in range(1, count + 1):
        arr.append(Note("Заметка " + str(i) + ": ", "Текст заметки №" + str(i)))
    return arr


def printArray(arr):
    for i in range(0, len(arr)):
        outString(arr[i])
        # print()


# =================== Основной блок =================================

os.system("CLS")
print("-------------------------------- program start -------------")
# my_array = makeArray(4)

work_array = readFromCSV("notes.csv")
print("-------------------------------- loaded from file -------------")
saveToCSV(work_array, "notes.bak")
print("-------------------------------- saved in bak -------------")

# printArray(work_array)
print("-------------------------------- printet by printArray -------------")
print("Всего заметок: " + str(len(work_array)))
print()

# printArray(work_array)

work_array = main_Menu(work_array)
# work_array = mainMenu(work_array)
# saveToCSV(my_array)

# newArray = readFromCSV("notes.csv")

# printArray(work_array)
saveToCSV(work_array, "notes.csv")
