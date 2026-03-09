class Producto:
    def __init__(self, codigo, nombre, precio):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__precio = precio

  
    def get_codigo(self):
        return self.__codigo

    def set_codigo(self, codigo):
        self.__codigo = codigo

   
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_precio(self):
        return self.__precio

    def set_precio(self, precio):
        self.__precio = precio

    def __str__(self):
        return (f"Código: {self.__codigo} | "
                f"Producto: {self.__nombre} | "
                f"Precio: ${self.__precio:.2f}")