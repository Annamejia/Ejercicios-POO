class Cuidador:
    def __init__(self, nombre, anios_experiencia):
        self.__nombre = nombre
        self.__anios_experiencia = anios_experiencia

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_aniosExperiencia(self):
        return self.__anios_experiencia

    def set_aniosExperiencia(self, anios_experiencia):
        self.__anios_experiencia = anios_experiencia

    def __str__(self):
        return (f"Cuidador: {self.__nombre} | "
                f"Experiencia: {self.__anios_experiencia} años")