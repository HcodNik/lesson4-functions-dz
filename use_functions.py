import datetime
from datetime import date
"""
МОДУЛЬ 3
Программа "Личный счет"
Описание работы программы:
Пользователь запускает программу у него на счету 0
Программа предлагает следующие варианты действий
1. пополнить счет
2. покупка
3. история покупок
4. выход

1. пополнение счета
при выборе этого пункта пользователю предлагается ввести сумму на сколько пополнить счет
после того как пользователь вводит сумму она добавляется к счету
снова попадаем в основное меню

2. покупка
при выборе этого пункта пользователю предлагается ввести сумму покупки
если она больше количества денег на счете, то сообщаем что денег не хватает и переходим в основное меню
если денег достаточно предлагаем пользователю ввести название покупки, например (еда)
снимаем деньги со счета
сохраняем покупку в историю
выходим в основное меню

3. история покупок
выводим историю покупок пользователя (название и сумму)
возвращаемся в основное меню

4. выход
выход из программы

При выполнении задания можно пользоваться любыми средствами

Для реализации основного меню можно использовать пример ниже или написать свой
"""

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
    print(f'Пополнение на сумму {float(add_money)} руб. выполнено успешно.')
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
    elif float(purchase_sum) <= 0:
        print('Сумма не может быть равна нулю!')
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
    return shopping_book


def menu_func(): # главное меню
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
            if shopping_book == []:
                print('История пуста...')
            print('Дата.....................Сумма..............Наименование операции')
            for i in range(len(shopping_book)):
                print(f'{shopping_book[i][0]}...............{shopping_book[i][2]}...............{shopping_book[i][1]}')
            menu_func()
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')

menu_func()





