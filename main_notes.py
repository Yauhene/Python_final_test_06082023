from datetime import datetime
from menu import main_Menu
from Note import *
from dump import *
import os

# =================== Основной блок =================================

os.system("CLS")

work_array = readFromCSV("notes.csv")
saveToCSV(work_array, "notes.bak")
print("Всего заметок: " + str(len(work_array)))
print()
work_array = main_Menu(work_array)
saveToCSV(work_array, "notes.csv")
