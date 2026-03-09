from Vehiculo import Vehiculo
class Acuaticos(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros, tipo_propulsion):
        super().__init__(marca, modelo, capacidad_pasajeros)
        self.__tipo_propulsion = tipo_propulsion

  
    def GetTipo_Propulsion(self):
        return self.__tipo_propulsion

    def SetTipo_Propulsion(self, tipo_propulsion):
        self.__tipo_propulsion = tipo_propulsion

    def Anclar(self):
        return f"{self.GetMarca()} {self.GetModelo()} ha lanzado el ancla."

    def Mover(self):
        return f"{self.GetMarca()} {self.GetModelo()} se está moviendo por agua con propulsión {self.__tipo_propulsion}."

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Propulsión: {self.__tipo_propulsion}")
