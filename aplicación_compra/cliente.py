from usuario import Usuario
from carrito import Carrito

class Cliente(Usuario):

    def __init__(self, name):
        super().__init__(name)
        self.carrito = Carrito(self)  # Cliente tiene un carrito asociado.

