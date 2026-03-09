class Animal:
    def __init__(self, nombre, edad, especie):
        self.__nombre = nombre
        self.__edad = edad
        self.__especie = especie

  
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

  
    def get_edad(self):
        return self.__edad

    def set_edad(self, edad):
        self.__edad = edad

  
    def get_especie(self):
        return self.__especie

    def set_especie(self, especie):
        self.__especie = especie

    def hacerSonido(self):
        pass

    def comer(self):
        return f"{self.__nombre} está comiendo."

    def __str__(self):
        return (f"Nombre: {self.__nombre} | "
                f"Edad: {self.__edad} años | "
                f"Especie: {self.__especie}")