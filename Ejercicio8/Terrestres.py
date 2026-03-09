from Vehiculo import Vehiculo
class Terrestres(Vehiculo):
    def __init__(self, marca, modelo, capacidad_pasajeros, num_ruedas):
        super().__init__(marca, modelo, capacidad_pasajeros)
        self.__num_ruedas = num_ruedas

    # Getters y Setters - Num_Ruedas
    def GetNum_Ruedas(self):
        return self.__num_ruedas

    def SetNum_Ruedas(self, num_ruedas):
        self.__num_ruedas = num_ruedas

    def Frenar(self):
        return f"{self.GetMarca()} {self.GetModelo()} está frenando."

    def Mover(self):
        return f"{self.GetMarca()} {self.GetModelo()} se está moviendo por tierra con {self.__num_ruedas} ruedas."

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Ruedas: {self.__num_ruedas}")
