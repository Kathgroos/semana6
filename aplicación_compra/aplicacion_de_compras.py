from cliente import Cliente
from articulo import Item
from vendedor import Vendedor

vendedor = Vendedor("DIC Store")
for i in range(10):
    Item("CPU", 40830, vendedor)
    Item("Memoria", 13880, vendedor)
    Item("Placa Madre", 28980, vendedor)
    Item("Fuente de Poder", 8980, vendedor)
    Item("Caja de PC", 8727, vendedor)
    Item("HDD 3.5 pulgadas", 10980, vendedor)
    Item("SSD 2.5 pulgadas", 13370, vendedor)
    Item("SSD M.2", 12980, vendedor)
    Item("Refrigerador de CPU", 13400, vendedor)
    Item("Tarjeta Gráfica", 23800, vendedor)

print("🤖 Introduce tu nombre")
cliente = Cliente(input())

print("🏧 Introduce la cantidad a depositar en tu billetera")
cliente.billetera.deposit(int(input()))

print("🛍️ Comenzando las compras")
finalizar_compras = False
while not finalizar_compras:
    print("📜 Lista de productos")
    vendedor.show_items()

    print("⛏ Introduce el número del producto")
    number = int(input())

    print("⛏ Introduce la cantidad del producto")
    quantity = int(input())

    items = vendedor.pick_items(number, quantity)
    for item in items:
        cliente.carrito.add(item)
    print("🛒 Contenido del carrito")
    cliente.carrito.show_items()
    print(f"🤑 Total: {cliente.carrito.total_amount()}")

    print("😭 ¿Deseas finalizar las compras? (yes/no)")
    finalizar_compras = input() == "yes"

print("💸 ¿Deseas confirmar la compra? (yes/no)")
if input() == "yes":
    cliente.carrito.check_out()

print("୨୧┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈Resultados┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈┈୨୧")
print(f"️🛍️ ️Propiedades de {cliente.name}")
cliente.show_items()
print(f"😱👛 Saldo de {cliente.name}: {cliente.billetera.balance}")

print(f"📦 Inventario de {vendedor.name}")
vendedor.show_items()
print(f"😻👛 Saldo de {vendedor.name}: {vendedor.billetera.balance}")

print("🛒 Contenido del carrito")
cliente.carrito.show_items()
print(f"🌚 Total: {cliente.carrito.total_amount()}")

print("🎉 Fin")

