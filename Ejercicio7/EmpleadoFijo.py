from Empleado import Empleado
class EmpleadoFijo(Empleado):
    def __init__(self, nombre, id, salario_base):
        super().__init__(nombre, id, salario_base)

    def Calcular_Salario(self):
        return self.get_salario_base()

    def __str__(self):
        return (f"Nombre: {self.get_Nombre()} | "
                f"ID: {self.get_Id()} | "
                f"Salario Base: ${self.get_salario_base()} | "
                f"Salario Final: ${self.Calcular_Salario()}")
