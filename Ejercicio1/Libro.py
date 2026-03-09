class Libro: 
    def __init__(self, titulo, autor, anio_publicacion, isbn, disponible):
        self.__titulo = titulo
        self.__autor = autor
        self.__anio_publicacion = anio_publicacion
        self.__isbn = isbn
        self.__disponible = disponible
        self.__veces_prestado = 0
    
    def set_titulo(self, nuevo_titulo):
        self.__titulo = nuevo_titulo
    def get_titulo(self):
        return self.__titulo
    
    def set_autor(self, nuevo_autor): 
         self.__autor = nuevo_autor
    def get_autor(self):
         return self.__autor

    def get_anio_publicacion(self):
         return self.__anio_publicacion

    def get_isbn(self):
         return self.__isbn

    def set_disponible(self, nuevo_disponible):
         self.__disponible = nuevo_disponible
    
    def get_disponible(self):
         return self.__disponible
    
    def get_veces_prestado(self):
         return self.__veces_prestado
 
    def __str__(self):
        return f"{self.__titulo} por {self.__autor} ({self.__anio_publicacion})-ISBN: {self.__isbn} - {'Disponible' if self.__disponible else 'No disponible'}"
    
    def cambiar_disponibilidad(self):
         if self.__disponible:
              self.__disponible = False
              self.__veces_prestado += 1
              return f"El libro '{self.__titulo}' ahora está prestado."
         else:
            self.__disponible = True
            return f"El libro '{self.__titulo}' ahora está disponible."