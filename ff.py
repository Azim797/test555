names = ('Oleg','Ivan')
# создаю меню
a = input('выберите действие:  1 - добавить\n  2- увидеть\n  3 - удалить\n 4 - изменить\n')
if a == '1':
    name = input ('введите имя для нового контакта\n:')
    # проверяю есть ли это имя в моем списке контактов
    # если  имя есть, то вывожу что имя занято
    print('имя занято')
    # если имя не занято
    # else:
    # добавляю имя в список
    names.append(name)
    print(f' {name}добавлен в список контактов\n ')
    print(names)
elif a == '2':
    print(names)
elif a == '3':
    # смотрю какой контакт хотят удалить
    names.remove (names)
    # удаляю контакт
    print(f'контакт удален\n')
    print(names)
elif a == '4':
    # name input[]
    name[0] = input()
    print(f'контакт изменен\n')
    print(names)