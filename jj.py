usernames = []
while True:
    username = input('Введите имя\n')
    if username.lower() in [i.lower() for i in usernames]:
        print(f'имя занято')
    elif username not in usernames:
        usernames.append(username)
    print(f'Добавлен{usernames}')

