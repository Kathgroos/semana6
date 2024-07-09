from poseible import Ownable

class Carrito(Ownable):
    from administrador_de_elemento import show_items

    def __init__(self, owner):
        self.set_owner(owner)
        self.items = []

    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)

    def check_out(self):
        if self.owner.billetera.balance < self.total_amount():
            raise ValueError("Fondos insuficientes")

        for item in self.items:
            self.owner.billetera.withdraw(item.price)
            item.owner.billetera.deposit(item.price) 
            item.owner = self.owner
    
        self.items = []






