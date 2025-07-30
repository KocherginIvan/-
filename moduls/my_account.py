def my_account(account = 0, dictionary= {'покупка': [],
                                        'цена': []}):

    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')
        choice = input('Выберите пункт меню ')
        if choice == '1':
            print(f'Сейчас на счету: {account}')
            adding = input('Пополнить счет на сумму: ')
            account += int(adding)
            pass
        elif choice == '2':
            purchase_amount = input('Сумма покупки: ')
            if account < int(purchase_amount):
                print('Недостаточно средств')
            else:
                purchase_name = input('Наименование покупки: ')
                dictionary['покупка'] += [purchase_name]
                dictionary['цена'] += [int(purchase_amount)]
                account -= int(purchase_amount)
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
