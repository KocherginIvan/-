from moduls.my_account import change_account, change_dictionary_purchase
from moduls.victory import rand_num
from moduls.dir_fil_change import create_dir, create_file, del_dir, del_file, copy_file, list_dir_file
from moduls.write_read_json import create_json , read_data_json

import os

def test_change_account():
    assert change_account(account=1000, add_accout=100, turn_accout=0) == 1100
    assert change_account(account=1000, add_accout=0, turn_accout=100) == 900
def test_add_purchases():
    assert change_dictionary_purchase(dictionary= {'покупка': [], 'цена': []}, add_purchase = ['pen'], add_price = [100]) == {'покупка': ['pen'], 'цена': [100]}
# def rand_num(num_list, count=5):
#     rand = random.sample(num_list, 5)
#     return rand
def test_rand_num():
    assert len(rand_num([0,1,2,3,4,5,6,7,8,9], 5)) == 5
    test_list = []
    for i in range(800):
        if 0 not in rand_num([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], 5):
            a = True
            break
    assert a == True
'''Тестирование "грязных" функций'''
def test_create_dir():
    create_dir('test')
    assert 'test' in os.listdir()
def test_create_file():
    create_file('test.txt')
    assert 'test.txt' in os.listdir()
def test_del_dir():
    del_dir('test')
    assert 'test' not in os.listdir()
def test_copy_file():
    copy_file('test.txt', 'test_1.txt')
    assert 'test_1.txt' in os.listdir()
def test_del_file_1():
    del_file('test.txt')
    assert 'test.txt' not in os.listdir()
def test_del_file_2():
    del_file('test_1.txt')
    assert 'test_1.txt' not in os.listdir()
def test_create_json():
    dict = {'1': [1]}
    create_json(dict, 'test')
    assert 'test.json' in os.listdir()
def test_read_data_json():
    data = read_data_json('test')
    assert data == {'1': [1]}
    del_file('test.json')
def test_list_dir_file():
    list_dir_file()
    f = open('list_dir.txt', 'r', encoding='utf-8')
    lines = f.read().splitlines()
    f.close()
    data = lines[1].split(': ')[1].split(', ') + \
           lines[0].split(': ')[1].split(', ')
    assert sorted(data) == sorted(os.listdir())
    del_file('list_dir.txt')