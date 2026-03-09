from Curso import Curso 
from Estudiante import Estudiante

curso1 = Curso(1, "Bases de Datos", "BD-101", 4)
curso2 = Curso(2, "Programación Orientada a Objetos", "POO-202", 3)
curso3 = Curso(3, "Redes de Computadores", "RC-303", 3)

estudiante1 = Estudiante(1, "Laura Gómez", "SENA-2024-001", "Análisis y Desarrollo de Software")
estudiante2 = Estudiante(2, "Sofia Marquez", "SENA-2023-008", "Administración")
estudiante3 = Estudiante(3, "Ely Marquez", "SENA-2024-006", "Análisis y Desarrollo de Software")


print("=" * 50)
print(estudiante1)
print(estudiante2)
print(estudiante3)
print("=" * 50)


print("\n Matriculando cursos...\n")
estudiante1.Matricular(curso1)
estudiante2.Matricular(curso2)
estudiante3.Matricular(curso3)
estudiante1.Matricular(curso1)
estudiante2.Matricular(curso3)


print("\n Cursos matriculados:")
for curso in estudiante1.get_curso():
    print(f"{curso}")

print("\n Cursos matriculados:")
for curso in estudiante2.get_curso():
    print(f"{curso}")

print("\n Cursos matriculados:")
for curso in estudiante3.get_curso():
    print(f"{curso}")