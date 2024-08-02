class Animal:
    def __init__(self,make_sound):
        self.make_sound=make_sound
    def make_sound(self,sound):
        print(sound)
class Cat(Animal):
    pass
cat = Cat()
cat.make_sound('мяу')

class Dog(Animal):
    pass
dog =Dog()
dog.make_sound('гав')
class Cow(Animal):
    pass
cow = Cow()
cow.make_sound('mu')
while True:
    menu = input('введите действие:''1 - звук кота''2- звук собаки''3 - звук коровы')
    if menu == '1':
        print(cat.make_sound())
    elif menu == '2':
        print(dog.make_sound())
    elif menu =='3':
        print(cow.make_sound())














