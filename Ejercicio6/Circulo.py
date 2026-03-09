import math
from FormaGeometrica import FormaGeometrica

class Circulo(FormaGeometrica):
    def __init__(self, color, radio):
        super().__init__(color, formula="π × r²")
        self.__radio = radio
        self.__pi = math.pi

    def get_radio(self):
        return self.__radio

    def set_radio(self, radio):
        self.__radio = radio

    def get_Pi(self):
        return self.__pi

    def set_Pi(self, pi):
        self.__pi = pi

    def calcular_area(self):
        return self.__pi * self.__radio ** 2

    def mostrarInformacion(self):
        print(f"\n{'='*35}")
        print(f"  Figura    : Círculo")
        super().mostrarInformacion()
        print(f"  Radio     : {self.__radio}")
        print(f"  Pi        : {self.__pi:.5f}")
        print(f"{'='*35}\n")