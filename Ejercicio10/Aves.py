from Animal import Animal


class Aves(Animal):
    def __init__(self, nombre, edad, especie, envergadura_alas):
        super().__init__(nombre, edad, especie)
        self.__envergadura_alas = envergadura_alas

    def get_envergaduraAlas(self):
        return self.__envergadura_alas

    def set_envergaduraAlas(self, envergadura_alas):
        self.__envergadura_alas = envergadura_alas

    def volar(self):
        return f"{self.get_nombre()} está volando con alas de {self.__envergadura_alas} cm."

    def hacerSonido(self):
        return f"{self.get_nombre()} está cantando."

    def __str__(self):
        return (f"{super().__str__()} | "
                f"Envergadura: {self.__envergadura_alas} cm")