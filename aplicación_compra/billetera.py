from poseible import Ownable

class Billetera(Ownable):

    def __init__(self, owner):
        self.set_owner(owner)
        self.balance = 0

    def deposit(self, amount):
        self.balance += int(amount)

    def withdraw(self, amount):
        if not self.balance >= amount:
            raise ValueError("Fondos insuficientes")
        self.balance -= int(amount)
        return amount



