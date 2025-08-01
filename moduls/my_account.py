def change_account(account, add_accout = 0, turn_accout = 0):
    account_1 = account + add_accout - turn_accout
    return account_1
def change_dictionary_purchase(dictionary = {'покупка': [],'цена': []}, add_purchase = [], add_price = []):
    dictionary['покупка'] += add_purchase
    dictionary['цена'] += add_price
    return dictionary
def my_account(account = 0, dictionary= {'покупка': [],'цена': []}):
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню ')
        if choice == '1':
            print(f'Сейчас на счету: {account}')
            adding = input('Пополнить счет на сумму: ')
            account = change_account(account, add_accout = int(adding), turn_accout = 0)
            pass
        elif choice == '2':
            purchase_amount = input('Сумма покупки: ')
            if account < int(purchase_amount):
                print('Недостаточно средств')
            else:
                purchase_name = input('Наименование покупки: ')
                dictionary = change_dictionary_purchase(dictionary=dictionary, add_purchase=[purchase_name], add_price=[int(purchase_amount)])
                account = change_account(account, add_accout = 0, turn_accout = int(purchase_amount))
            pass
        elif choice == '3':
            print('История Ваших покупок: \n')
            for i in range(len(dictionary['покупка'])):
                print(f'Наименование: {dictionary['покупка'][i]}\n Стоимость: {dictionary['цена'][i]}\n')
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')
    return account, dictionary
