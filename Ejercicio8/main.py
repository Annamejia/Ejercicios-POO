from Terrestres import Terrestres
from Acuaticos import Acuaticos

print("         SISTEMA DE GESTIÓN DE VEHÍCULOS")
 
vehiculo1 = Terrestres("Toyota", "Corolla", 5, 4)
vehiculo2 = Terrestres("Ford", "F-150", 3, 4)
vehiculo3 = Acuaticos("Yamaha", "FX Cruiser", 2, "Motor Jet")
vehiculo4 = Acuaticos("Sea Ray", "Sundancer", 8, "Motor Inborda")

vehiculos = [vehiculo1, vehiculo2, vehiculo3, vehiculo4]


print("\n LISTA DE VEHÍCULOS:")

for vehiculo in vehiculos:
    tipo = "Terrestre" if isinstance(vehiculo, Terrestres) else "Acuático"
    print(f"[{tipo}] {vehiculo}")

print("\n MOVIMIENTO DE VEHÍCULOS:")

for vehiculo in vehiculos:
    print(vehiculo.Mover())

print("\n MÉTODOS EXCLUSIVOS:")

print(vehiculo1.Frenar())
print(vehiculo2.Frenar())
print(vehiculo3.Anclar())
print(vehiculo4.Anclar())


print("\n ACTUALIZANDO DATOS...")
vehiculo1.SetMarca("Toyota")
vehiculo1.SetModelo("Camry")
vehiculo1.SetCapacidadPasajeros(6)
vehiculo3.SetTipo_Propulsion("Turbina")
print("- vehiculo1 actualizado: Toyota Camry, capacidad 6")
print("- vehiculo3 propulsión actualizada: Turbina")

   
print("\n LISTA ACTUALIZADA:")
for vehiculo in vehiculos:
    tipo = "Terrestre" if isinstance(vehiculo, Terrestres) else "Acuático"
    print(f"[{tipo}] {vehiculo}")

