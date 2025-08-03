import os
import sys
import moduls.dir_fil_change as dfc
from moduls.victory import victory
from moduls.my_account import my_account
account = 0
dictionary = {'покупка': [],
              'цена': []}
while True:
    arg = input('''1. Создать папку
2. Удалить (файл/папку) 
3. Копировать (файл/папку) 
4. Просмотр содержимого рабочей директории 
5. Сохранить содержимое рабочей директории в файл
6. Посмотреть только папки 
7. Посмотреть только файлы 
8. Просмотр информации об операционной системе 
9. Создатель программы 
10. Играть в викторину 
11. Мой банковский счет 
12. Смена рабочей директории 
13. Выход \n''')
    if arg == '1':
        dir_name = input('Введите имя создаваемой папки: ')
        dfc.create_dir(dir_name)
    if arg == '2':
        name = input('Введите имя файла/директории которую нужно удалить: ')
        if '.' in name:
            dfc.del_file(name)
        else:
            dfc.del_dir(name)
    if arg == '3':
        file_name = input('Введите имя файла который нужно копировать: ')
        file_name_new = input('Введите имя файла для копии файла: ')
        dfc.copy_file(file_name, file_name_new)
    if arg == '4':
        print(*os.listdir())
    if arg == '5':
        dfc.list_dir_file()
    if arg == '6':
        for i  in os.listdir():
            if '.' not in i:
                print(f'{i}')
    if arg == '7':
        for i in os.listdir():
            if '.' in i:
                print(f'{i}')
    if arg == '8':
        os_detail = sys.platform
        print(f'Ваша система: {sys.platform}\nИмя системы: {os.name}')
    if arg == '9':
        print('Программу создал Иван Кочергин')
    if arg == '10':
        victory()
    if arg == '11':
        account, dictionary = my_account(account, dictionary)
    if arg == '12':
        ch_dir = input('Введите путь к директории: ')
        if ch_dir.startswith(':', 2) or ch_dir.startswith('/'):
            os.chdir(ch_dir)
        else:
            os.chdir(ch_dir)
    if arg == '13':
        break