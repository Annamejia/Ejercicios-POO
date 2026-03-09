from Circulo import Circulo
from Rectangulo import Rectangulo

circulo1 = Circulo("Rojo", 5)
circulo1.mostrarInformacion()

rectangulo1 = Rectangulo("Azul", 8, 4)
rectangulo1.mostrarInformacion()

print("== Modificando atributos ==")
circulo1.set_Color("Verde")
circulo1.set_radio(7)
print(f"Nuevo color: {circulo1.get_Color()}")
print(f"Nuevo radio: {circulo1.get_radio()}")
print(f"Nueva área : {circulo1.calcular_area():.2f}")

rectangulo1.set_largo(10)
rectangulo1.set_ancho(3)
print(f"\nNuevo largo: {rectangulo1.get_largo()}")
print(f"Nuevo ancho: {rectangulo1.get_ancho()}")
print(f"Nueva área : {rectangulo1.calcular_area():.2f}")