import datetime
from datetime import date


wallet = 5000.0
shopping_book = []

def curent_date(): # текущая дата
    current_date = str(date.fromisoformat('2019-01-01').today())
    return current_date
def adding_wallet_func(): # пополнение счёта
    global wallet
    add_money = input('Введите сумму пополнения в рублях: ')
    while add_money.isdigit() != True:
        print('Некоректный ввод! Повторите попытку.')
        return adding_wallet_func()
    wallet += float(add_money)
    print(f'Пополнение на сумму {add_money} руб. выполнено успешно.')
    return menu_func()

def buy_func(): # Покупка
    global wallet
    purchase_sum = input('Введите сумму покупки в рублях: ')
    while purchase_sum.isdigit() != True:
        print('Некоректный ввод! Повторите попытку.')
        return buy_func()
    if float(purchase_sum) > wallet:
        print('Недостаточно средств!')
        menu_func()
    else:
        purchase_name = input('Введите название покупки: ')
        wallet -= float(purchase_sum)
        history_func(purchase_name, purchase_sum)
        return menu_func()

def history_func(purchase_name, purchase_sum): # история покупок
    global shopping_book
    current_purchase = [curent_date(), purchase_name, purchase_sum]
    shopping_book.append(current_purchase)
    for i in range(len(shopping_book)):
        print(shopping_book[i])
    return shopping_book


def menu_func():
    while True:
        print(f'Текущий баланс: {wallet} руб.')
        print(f'1. пополнение счета.')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        choice = input('Выберите пункт меню: ')
        if choice == '1':
            adding_wallet_func()
        elif choice == '2':
            buy_func()
        elif choice == '3':
            pass
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

#buy_func()
#curent_date()
#history_func('еда',100)

a1 = [['2023-11-14', 'еда', 100]]
print(a1[0])