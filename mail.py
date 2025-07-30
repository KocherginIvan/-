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
5. Посмотреть только папки 
6. Посмотреть только файлы 
7. Просмотр информации об операционной системе 
8. Создатель программы 
9. Играть в викторину 
10. Мой банковский счет 
11. Смена рабочей директории 
12. Выход \n''')
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
        for i  in os.listdir():
            if '.' not in i:
                print(f'{i}')
    if arg == '6':
        for i in os.listdir():
            if '.' in i:
                print(f'{i}')
    if arg == '7':
        os_detail = sys.platform
        print(f'Ваша система: {sys.platform}\nИмя системы: {os.name}')
    if arg == '8':
        print('Программу создал Иван Кочергин')
    if arg == '9':
        victory()
    if arg == '10':
        account, dictionary = my_account(account, dictionary)
    if arg == '11':
        ch_dir = input('Введите путь к директории: ')
        if ch_dir.startswith(':', 2) or ch_dir.startswith('/'):
            os.chdir(ch_dir)
        else:
            os.chdir(ch_dir)
    if arg == '12':
        break