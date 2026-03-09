class Vehiculo:
    def __init__(self, marca, modelo, capacidad_pasajeros):
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad_pasajeros = capacidad_pasajeros

    # Getters y Setters - Marca
    def GetMarca(self):
        return self.__marca

    def SetMarca(self, marca):
        self.__marca = marca

    # Getters y Setters - Modelo
    def GetModelo(self):
        return self.__modelo

    def SetModelo(self, modelo):
        self.__modelo = modelo

    # Getters y Setters - CapacidadPasajeros
    def GetCapacidadPasajeros(self):
        return self.__capacidad_pasajeros

    def SetCapacidadPasajeros(self, capacidad_pasajeros):
        self.__capacidad_pasajeros = capacidad_pasajeros

    def Mover(self):
        pass

    def __str__(self):
        return (f"Marca: {self.__marca} | "
                f"Modelo: {self.__modelo} | "
                f"Capacidad: {self.__capacidad_pasajeros} pasajeros")
