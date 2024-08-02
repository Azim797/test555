class Player:
    def __init__(self,name,number):
        self.name = name
        self.number = number
class Napadaushiy(Player):
    def __init__(self,fast,kick,pas):
        super().__init__(fast,kick)
        self.pas = pas

