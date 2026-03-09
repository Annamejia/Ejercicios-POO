from Mamifero import Mamifero
from Aves import Aves
from Cuidador import Cuidador
from Jaula import Jaula


print("         SISTEMA DE GESTIÓN DE ZOOLÓGICO")

c1 = Cuidador("Carlos Ruiz", 8)
c2 = Cuidador("María López", 5)

m1 = Mamifero("León", 6, "Panthera leo", "Corto y dorado")
m2 = Mamifero("Tigre", 4, "Panthera tigris", "Rayado naranja")
a1 = Aves("Águila", 3, "Aquila chrysaetos", 220)
a2 = Aves("Loro", 2, "Amazona ochrocephala", 45)

j1 = Jaula(1, 3, c1)
j2 = Jaula(2, 2, c2)

print("\n AGREGANDO ANIMALES A JAULAS:")
print("-" * 55)
print(j1.agregar_animal(m1))
print(j1.agregar_animal(m2))
print(j2.agregar_animal(a1))
print(j2.agregar_animal(a2))

  
j1.mostrar_info()
j2.mostrar_info()

print("\n SONIDOS Y ALIMENTACIÓN:")
print("-" * 55)
for animal in [m1, m2, a1, a2]:
    print(animal.hacerSonido())
    print(animal.comer())

   
print("\n MÉTODOS EXCLUSIVOS:")
print("-" * 55)
print(m1.amamantan())
print(m2.amamantan())
print(a1.volar())
print(a2.volar())

print("\n  ACTUALIZANDO DATOS...")
print("-" * 55)
c1.set_aniosExperiencia(10)
m1.set_edad(7)
a1.set_envergaduraAlas(230)
print(f"- Experiencia de Carlos: {c1.get_aniosExperiencia()} años")
print(f"- Nueva edad del León: {m1.get_edad()} años")
print(f"- Nueva envergadura del Águila: {a1.get_envergaduraAlas()} cm")
