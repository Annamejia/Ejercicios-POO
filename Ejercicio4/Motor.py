class Motor:
    def __init__(self, cilindrada, tipo_combustible, potencia):
        self.__cilindrada = cilindrada
        self.__tipo_combustible = tipo_combustible
        self.__potencia = potencia
    
    def set_cilindrada(self, nueva_cilindrada):
        if nueva_cilindrada > 0:
            self.__cilindrada = nueva_cilindrada
        else:
            print("Error: la cilindrada debe ser mayor a 0")
    def get_cilindrada(self):
        return self.__cilindrada
    
    def set_tipo_combustible(self, nuevo_tipo_conbustible):
        self.__tipo_combustible = nuevo_tipo_conbustible
    def get_tipo_combustible(self):
        return self.__tipo_combustible
    
    def set_potencia(self, nueva_potencia):
        if nueva_potencia > 0:
            self.__potencia = nueva_potencia
        else:
            print("Error: la potencia debe ser mayor a 0")
    def get_potencia(self):
        return self.__potencia
    
    def mostrar_info(self):
        print(f"  Cilindrada: {self.__cilindrada}")
        print(f"  Tipo Combustible: {self.__tipo_combustible}")
        print(f"  Potencia: {self.__potencia}")