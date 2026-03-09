from Animal import Animal

class Mamifero(Animal):
    def __init__(self, nombre, edad, especie, tipo_pelaje):
        super().__init__(nombre, edad, especie)
        self.__tipo_pelaje = tipo_pelaje

  
    def get_tipoPelaje(self):
        return self.__tipo_pelaje

    def set_tipoPelaje(self, tipo_pelaje):
        self.__tipo_pelaje = tipo_pelaje

    def amamantan(self):
        return f"{self.get_nombre()} amamanta a sus crías."

    def hacerSonido(self):
        return f"{self.get_nombre()} emite un sonido de mamífero."

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Pelaje: {self.__tipo_pelaje}")