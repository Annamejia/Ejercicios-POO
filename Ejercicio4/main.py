from Motor import Motor
from Automovil import Automovil

motor1 = Motor(1800, "Gasolina", 140)
motor2 = Motor(1700, "Gasolina", 150)
motor3 = Motor(1500, "Gasolina", 160)

auto1 = Automovil("Toyota", "Corolla", 2021, "Rojo", motor1)
auto2 = Automovil("Chevrolet", "Corolla", 2022, "Negro", motor2)
auto3 = Automovil("Volkswagen", "Corolla", 2023, "Azul", motor3)

auto1.mostrar_info()
auto2.mostrar_info()
auto3.mostrar_info()