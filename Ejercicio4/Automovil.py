from Motor import Motor
class Automovil:
    def __init__(self, marca, modelo, anio, color, motor):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        self.__color = color
        self.__motor = motor

    def get_marca(self):
        return self.__marca
    
    def get_modelo(self):
        return self.__modelo

    def get_anio(self):
        return self.__anio

    def set_color(self, nuevo_color):
        self.__color = nuevo_color
    def get_color(self):
        return self.__color

    def get_motor(self):
        return self.__motor

    def mostrar_info(self):
            print(f"Marca:  {self.__marca}")
            print(f"Modelo: {self.__modelo}")
            print(f"Año:    {self.__anio}")
            print(f"Color:  {self.__color}")
            print("Motor:")
            self.__motor.mostrar_info()