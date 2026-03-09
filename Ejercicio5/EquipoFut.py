from Jugador import Jugador

class EquipoFut:
    def __init__(self, nombre, ciudad, entrenador):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__entrenador = entrenador 
        self.__jugadores = []
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_cuidad(self, nueva_ciudad):
        self.__ciudad = nueva_ciudad
    def get_ciudad(self):
        return self.__ciudad
    
    def set_entrenador(self, nuevo_entrenador):
        self.__entrenador = nuevo_entrenador
    def get_entrenador(self):
        return self.__entrenador
    
    def agregar(self, jugador: Jugador):
        self.__jugadores.append(jugador)
        print(f"{jugador.get_nombre()} agregado al equipo {self.__nombre}.")

    def remover(self, jugador: Jugador):
        if jugador in self.__jugadores:
            self.__jugadores.remove(jugador)
            print(f"{jugador.get_nombre()} removido de {self.__nombre}.")
        else:
            print(f"{jugador.get_nombre()} no pertenece a {self.__nombre}.")


    def mostrar_plantilla(self):
        print(f"Equipo : {self.__nombre}")
        print(f"Ciudad : {self.__ciudad}")
        print(f"Entrenador : {self.__entrenador}")
        print(f"Plantilla ({len(self.__jugadores)} jugadores):")
        if not self.__jugadores:
            print("  (Sin jugadores registrados)")
        for jugador in self.__jugadores:
            print(jugador)
        

        