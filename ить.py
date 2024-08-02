class User:
    def __init__(self,name,number,mail):
        self.name = name
        self.number = number
        self.mail = mail
    def change_username(self,change):
        self.name = change(input('введите имя'))
        print('')
    def change_number(self,change):
        self.number = change(input('введите номер'))
        print('')
    def change_mail(self,change):
      self.mail = change(input('введите почту'))
      print('')
name = input(' введите имя\n')
number = int(input('введите номер\n'))
mail = input('введите почту\n')
print('вы зарегистрированы\n')
user = User(name,number,mail)
while True:
    menu = input('введите действие\n' '1 - изменить имя\n''2-изменить номер\n''3-изменить почту\n')
    if menu == '1':
        redact = input('введите изменение:')
        user.change_username(str(redact))
        print('')
    elif menu == '2':
        redact = input('введите изменение')
        user.change_number(int(redact))
        print('')
    elif menu =='3':
        redact  =input('введите изменение')
        user.change_mail(str(redact))
        print('')