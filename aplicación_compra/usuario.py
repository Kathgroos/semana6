from billetera import Billetera

class Usuario:
    from administrador_de_elemento import show_items, items_list, pick_items

    def __init__(self, name):
        self.name = name
        self.billetera = Billetera(self)  # Usuario tiene una billetera asociada.


