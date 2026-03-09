from Cuidador import Cuidador


class Jaula:
    def __init__(self, numero, capacidad, cuidador):
        self.__numero = numero
        self.__capacidad = capacidad
        self.__cuidador = cuidador   # objeto de tipo Cuidador
        self.__animales = []         # lista de objetos Animal

    # Getters y Setters - Numero
    def get_numero(self):
        return self.__numero

    def set_numero(self, numero):
        self.__numero = numero

    # Getters y Setters - Capacidad
    def get_capacidad(self):
        return self.__capacidad

    def set_capacidad(self, capacidad):
        self.__capacidad = capacidad

    def get_cuidador(self):
        return self.__cuidador

    def set_cuidador(self, cuidador):
        self.__cuidador = cuidador

    def get_animales(self):
        return self.__animales

    def set_animales(self, animales):
        self.__animales = animales

    def agregar_animal(self, animal):
        if len(self.__animales) < self.__capacidad:
            self.__animales.append(animal)
            return f"{animal.get_nombre()} agregado a la jaula {self.__numero}."
        return f"Jaula {self.__numero} llena. Capacidad máxima: {self.__capacidad}."

    def mostrar_info(self):
        print(f"\n JAULA #{self.__numero} | Capacidad: {self.__capacidad}")
        print(f"   {self.__cuidador}")
        print(f"   {'─' * 45}")
        for animal in self.__animales:
            print(f"   {animal}")
        print(f"   Total animales: {len(self.__animales)}/{self.__capacidad}")

    def __str__(self):
        return (f"Jaula #{self.__numero} | "
                f"Capacidad: {self.__capacidad} | "
                f"Animales: {len(self.__animales)} | "
                f"Cuidador: {self.__cuidador.get_nombre()}")