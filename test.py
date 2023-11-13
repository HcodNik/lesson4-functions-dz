wallet = 500.0 # всего на счету, по умолчанию - 0.0

def adding_wallet_func():
    global wallet
    add_money = input('Введите сумму пополнения в рублях: ')
    while add_money.isdigit() != True:
        print('Некоректный ввод! Повторите попытку.')
        return adding_wallet_func()
    wallet += float(add_money)
    print(f'Пополнение на сумму {add_money} руб. выполнено успешно.')
    print(f'Текущий баланс: {wallet} руб.')
    return wallet

def menu_func():
    while True:
        print(f'1. пополнение счета.')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            adding_wallet_func()
            return menu_func()
        elif choice == '2':
            pass
        elif choice == '3':
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

menu_func()