from ph import *
import os

# Функция главного меню ==================================
def mainMenu(fileContent, pos):
    tempList = list()
    
    getOut=False # флаг для выхода из меню
    while getOut != True:
        os.system('CLS')
        prAbonents(fileContent)
        
        print('==================================================')
        print('Выберите пункт меню, нажав соответствующую цифру и Enter. ')
        print('1. Найти абонента/Изменить запись/Удалить абонента')
        print('2. Вывести полный список абонентов')
        print('3. Добавить нового абонента')
        print('4. Сохранить изменения')
        print('Q/q - Выйти из программы')
        choice = input('Ваш выбор: ')
        choice = choice.lower()
        if choice == 'Q' or choice == 'q' or choice == 'й' or choice == 'Й':
            getOut = True
            saveFile(fileContent, 'phones.txt')
            print()
            print('Дело хозяйское... До новых встреч!')
            print()
        if choice == '1':
            fileContent = findAb(fileContent)
            
        if choice == '2':
            prAbonents(readFile('phones.txt'))

        if choice == '3':
            fileContent = addAb(readFile('phones.txt'))

        if choice == '4':
            saveFile(fileContent, 'phones.txt')

    return fileContent    
            
            