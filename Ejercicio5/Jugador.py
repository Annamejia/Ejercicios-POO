class Jugador: 
    def __init__(self, id, nombre, edad, posicion, numeroCamisa):
        self.__id = id
        self.__nombre = nombre
        self.__edad = edad 
        self.__posicion = posicion
        self.__numeroCamisa = numeroCamisa

    def get_id(self):
        return self.__id

    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_edad(self, nueva_edad):
        self.__edad = nueva_edad
    def get_edad(self):
        return self.__edad

    def set_posicion(self, nueva_posicion):
        self.__posicion = nueva_posicion
    def get_posicion(self):
        return self.__posicion

    def set_numeroCamisa(self, nuevo_nuemeroCamisa):
        self.__numeroCamisa = nuevo_nuemeroCamisa
    def get_numeroCamisa(self):
        return self.__numeroCamisa
    
    def transferir(self, nuevo_equipo):
        print(f"{self.__nombre} ha sido transferido al equipo {nuevo_equipo.get_nombre()}.")

    def __str__(self):
        return(f"Numero de Camiseta: {self.__numeroCamisa} | Nombre: {self.__nombre}"
               f" | Edad:{self.__edad} | Posición: {self.__posicion}")



