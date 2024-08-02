sklad = {}
korzina = {}
while True:
    menu = input('Выберите действие:\n' '1 - Добавить:\n'  '2 - Продукты:\n' '3 - Корзина:\n' '4 - Удалить:\n' 
                 '5 - Изменить:\n')
    if menu == '1':
        name = input('Введите название продукта\n')
        count = input('Выберите количество продукта\n')
        if name in sklad.keys():
            print('Такой продукт есть\n')
        else:
            sklad[name] = int(count)
            korzina[name] = int(count)
            print(f'Добавлено в корзину')
    elif menu == '2':
        for k,v in sklad.items():
            print(f'{k}:{v} кг')
    elif menu == '3':
        for k,v in korzina.items():
            print(f'{k}:{v} ')
    elif menu == '4':
        print(' удалите')
        korzina.pop(input())
        print('удалено')
    elif menu == '5':
        korzina.pop(input('Введите  название то что хотели изменить'))
        input('введите изменение')
        int(input('введите количество'))
        print('Изменено')


