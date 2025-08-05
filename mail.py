import os
import sys
import moduls.dir_fil_change as dfc
from moduls.victory import victory
from moduls.my_account import my_account
from moduls.decorator import add_seporator
@add_seporator
def print_name():
    print('Программу создал Иван Кочергин')
    pass
account = 0
dictionary = {'покупка': [],
              'цена': []}
while True:
    arg = int(input('''1. Создать папку
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
13. Выход \n'''))
    if arg == 1:
        try:
            dir_name = input('Введите имя создаваемой директории: ')
            dfc.create_dir(dir_name)
        except:
            print('Введено неправильное имя директории')
    if arg == 2:
        try:
            name = input('Введите имя файла/директории которую нужно удалить: ')
            if '.' in name:
                dfc.del_file(name)
            else:
                dfc.del_dir(name)
        except:
            print('Введено неправильное имя файла/директории')
    if arg == 3:
        try:
            file_name = input('Введите имя файла который нужно копировать: ')
            file_name_new = input('Введите имя файла для копии файла: ')
            dfc.copy_file(file_name, file_name_new)
        except:
            print('Введено неправильное имя файла или имя для копии файла')
    if arg == 4:
        print(*os.listdir())
    if arg == 5:
        dfc.list_dir_file()
    if arg == 6:
        print(*[f'{i}\n' for i in os.listdir() if '.' not in i])
    if arg == 7:
        print(*[f'{i}\n' for i in os.listdir() if '.' in i])
    if arg == 8:
        os_detail = sys.platform
        print(f'Ваша система: {sys.platform}\nИмя системы: {os.name}')
    if arg == 9:
        print_name()
    if arg == 10:
        victory()
    if arg == 11:
        account, dictionary = my_account(account, dictionary)
    if arg == 12:
        try:
            ch_dir = input('Введите путь к директории: ')
            os.chdir(ch_dir)
        except:
            print('Введен неправильный путь')
    if arg == 13:
        break
