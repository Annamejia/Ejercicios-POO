from Cliente import Cliente
from Producto import Producto

class Pedido:
    def __init__(self, cliente, fecha):
        self.__cliente = cliente  
        self.__total = 0
        self.__items = []         

    
    def get_cliente(self):
        return self.__cliente

    def set_cliente(self, cliente):
        self.__cliente = cliente

  
    def get_fecha(self):
        return self.__fecha

    def set_fecha(self, fecha):
        self.__fecha = fecha

  
    def get_total(self):
        return self.__total

    def set_total(self, total):
        self.__total = total

    
    def get_items(self):
        return self.__items

    def set_items(self, items):
        self.__items = items

   
    def agregar_producto(self, producto):
        self.__items.append(producto)
        self.__total += producto.get_precio()

    def eliminar_producto(self, codigo):
        for producto in self.__items:
            if producto.get_codigo() == codigo:
                self.__total -= producto.get_precio()
                self.__items.remove(producto)
                return f"Producto {codigo} eliminado del pedido."
        return f"Producto {codigo} no encontrado."

    def mostrar_resumen(self):
        print(f"\n PEDIDO - Fecha: {self.__fecha}")
        print(f"   {self.__cliente}")
        print(f"   {'─' * 40}")
        for item in self.__items:
            print(f"   {item}")
        print(f"   {'─' * 40}")
        print(f"   TOTAL: ${self.__total:.2f}")

    def __str__(self):
        return (f"Pedido [{self.__fecha}] | "
                f"Cliente: {self.__cliente.get_nombre()} | "
                f"Items: {len(self.__items)} | "
                f"Total: ${self.__total:.2f}")