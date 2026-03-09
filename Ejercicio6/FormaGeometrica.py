class FormaGeometrica:
    def __init__(self, color: str, formula: str, area: float = 0):
        self.__color = color
        self.__formula = formula
        self.__area = area

    def get_Color(self):
        return self.__color
    def set_Color(self, color):
        self.__color = color

    def get_Formula(self):
        return self.__formula
    def set_Formula(self, formula):
        self.__formula = formula

    def get_Area(self):
        return self.__area

    def set_Area(self, area):
        self.__area = area

    def calcular_area(self):
        """Será sobreescrito por las subclases."""
        pass

    def mostrarInformacion(self):
        print(f"  Color     : {self.__color}")
        print(f"  Fórmula   : {self.__formula}")
        print(f"  Área      : {self.calcular_area():.2f}")