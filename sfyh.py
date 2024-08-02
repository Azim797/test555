class BankAccount:
       def __init__(self,name,balance):
        self.name= name
        self.balance= balance
        def deposit(self,money_amount):
            self.balance = money_amount + self.balance
            print (f'счет пополнен на{money_amount}')
        def cash(self,money_amount):
            if  self.balance >= money_amount:
                self.balance= self.balance - money_amount
                print(f'вы сняли {money_amount}')
            else:
                print(f'недостаточно средств')
        def my_balance(self):
            print(f'у вас на счету{self.balance}')

client1 = BankAccount
name = input('')
print('Вы зарегистрированы\n')

while True:
    menu =()