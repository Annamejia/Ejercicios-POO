from Libro import Libro

libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967, "978-0-06-112008-4", True)
libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605, "978-84-376-0494-7", True)
libro3 = Libro("El amor en los tiempos del cólera", "Gabriel García Márquez", 1985, "978-0-7432-7356-5", True)
libro4 = Libro("La sombra del viento", "Carlos Ruiz Zafón", 2001, "978-84-08-04364-5", True)
libro5 = Libro("El nombre de la rosa", "Umberto Eco", 1980, "978-84-204-7953-1", True)

rae_libros = [libro1, libro2, libro3, libro4, libro5]

for Libro in rae_libros:
    print(Libro)

print(vars(libro1))
