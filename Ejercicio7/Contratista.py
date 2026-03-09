from Empleado import Empleado
class Contratista(Empleado):
    def __init__(self, nombre, id, salario_base, tarifa_hora, horas_trabajadas):
        super().__init__(nombre, id, salario_base)
        self.__tarifa_hora = tarifa_hora
        self.__horas_trabajadas = horas_trabajadas

    def get_tarifa_Hora(self):
        return self.__tarifa_hora

    def set_tarifa_Hora(self, tarifa_hora):
        self.__tarifa_hora = tarifa_hora

    def get_horas_trabajadas(self):
        return self.__horas_trabajadas

    def set_horas_trabajadas(self, horas_trabajadas):
        self.__horas_trabajadas = horas_trabajadas

    def Calcular_Salario(self):
        return self.get_salario_base() + (self.__tarifa_hora * self.__horas_trabajadas)
    
    def __str__(self):
        return (f"Nombre: {self.get_Nombre()} | "
                f"ID: {self.get_Id()} | "
                f"Tarifa por Hora: ${self.get_tarifa_Hora():.2f} | "
                f"Horas: {self.get_horas_trabajadas()} | "
                f"Salario Final: ${self.Calcular_Salario():.2f}")
