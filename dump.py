import json
from Note import Note
import csv


# class Test:
#     def __init__(self, title, body):
#         self.title = title
#         self.body = body


# def to_jsonN(obj):
#     if isinstance(obj, Note):
#         result = obj.__dict__
#         result["className"] = obj.__class__.__name__
#         return result


# def to_jsonT(obj):
#     if isinstance(obj, Test):
#         result = obj.__dict__
#         result["className"] = obj.__class__.__name__
#         return result


def makeArray(count):
    arr = []
    for i in range(1, count + 1):
        arr.append(
            Note("", "Заметка " + str(i) + ": ", "Текст заметки №" + str(i), "", "")
        )
    return arr


# def outString(n_):
#     print("id: " + str(n_.id) + "        " + str(n_.date_mark) + str(n_.time_mark))
#     print("====   ========" + str(n_.title) + str(n_.body))


# def printArray(arr):
#     for i in range(0, len(arr)):
#         outString(arr[i])
#         print()


# notes = makeArray(3)
# notes_from = []


def saveToCSV(array, file):
    # Записываем массив экземпляров Note в файл с разделителем ';'
    with open(file, "w", encoding="utf8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["id", "title", "body", "date_mark", "time_mark"])
        # Записываем заголовки столбцов
        for note in array:
            writer.writerow(
                [note.id, note.title, note.body, note.date_mark, note.time_mark]
            )  # Записываем значения заметок

    # Читаем данные из файла
    # with open("notes.csv", "r", encoding="utf8") as file:
    #     reader = csv.reader(file, delimiter=";")
    #     next(reader)  # Пропускаем заголовки столбцов
    #     for row in reader:
    #         id, title, body, date_mark, time_mark = row
    #         note = Note(id, title, body, date_mark, time_mark)
    #         notes_from.append(note)

    # print("Результирующий массив:")
    # printArray(notes_from)

    file.close()
    # return notes_from


def readFromCSV(file):
    # Читаем данные из файла
    with open("notes.csv", "r", encoding="utf8") as file:
        reader = csv.reader(file, delimiter=";")
        notes_from = []
        next(reader)  # Пропускаем заголовки столбцов
        for row in reader:
            id, title, body, date_mark, time_mark = row
            note = Note(id, title, body, date_mark, time_mark)
            notes_from.append(note)
    print("Прочитано из файла заметок: " + str(len(notes_from)))
    Note.units_num = len(notes_from)
    file.close()
    return notes_from
