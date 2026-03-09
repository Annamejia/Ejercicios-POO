from Cliente import Cliente
from Producto import Producto
from Pedido import Pedido


print(" SISTEMA DE GESTIÓN DE PEDIDOS")
 
cliente1 = Cliente("Ana García", "ana@email.com", "3001234567")
cliente2 = Cliente("Luis Pérez", "luis@email.com", "3109876543")

   
p1 = Producto("P001", "Laptop", 2500000)
p2 = Producto("P002", "Mouse", 45000)
p3 = Producto("P003", "Teclado", 120000)
p4 = Producto("P004", "Monitor", 850000)


pedido1 = Pedido(cliente1, "2026-03-08")
pedido2 = Pedido(cliente2, "2026-03-08")

    
pedido1.agregar_producto(p1)
pedido1.agregar_producto(p2)
pedido1.agregar_producto(p3)

pedido2.agregar_producto(p3)
pedido2.agregar_producto(p4)

    
pedido1.mostrar_resumen()
pedido2.mostrar_resumen()

print("\n  ACTUALIZANDO DATOS...")
print("-" * 55)
cliente1.set_email("ana.garcia@email.com")
cliente1.set_telefono("3007654321")
p1.set_precio(2300000)
print(f"- Email de Ana actualizado: {cliente1.get_email()}")
print(f"- Teléfono de Ana actualizado: {cliente1.get_telefono()}")
print(f"- Precio Laptop actualizado: ${p1.get_precio():.2f}")

    # Eliminar un producto del pedido
print("\n  ELIMINANDO PRODUCTO DEL PEDIDO 1...")
print("-" * 55)
print(pedido1.eliminar_producto("P002"))
pedido1.mostrar_resumen()

   
