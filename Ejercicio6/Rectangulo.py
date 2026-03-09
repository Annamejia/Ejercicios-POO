from FormaGeometrica import FormaGeometrica

class Rectangulo(FormaGeometrica):
    def __init__(self, color, largo, ancho):
        super().__init__(color, formula="Largo × Ancho")
        self.__largo = largo
        self.__ancho = ancho

    def get_largo(self):
        return self.__largo

    def set_largo(self, largo):
        self.__largo = largo

    def get_ancho(self):
        return self.__ancho

    def set_ancho(self, ancho):
        self.__ancho = ancho

    
    def calcular_area(self):
        return self.__largo * self.__ancho

    def mostrarInformacion(self):
        print(f"\n{'='*35}")
        print(f"  Figura    : Rectángulo")
        super().mostrarInformacion()
        print(f"  Largo     : {self.__largo}")
        print(f"  Ancho     : {self.__ancho}")
        print(f"{'='*35}\n")
