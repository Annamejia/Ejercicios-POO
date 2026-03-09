class Empleado:
    def __init__(self, nombre, id, salario_base):
        self.__nombre = nombre
        self.__id = id
        self.__salario_base = salario_base

    def get_Nombre(self):
        return self.__nombre

    def set_Nombre(self, nombre):
        self.__nombre = nombre

    def get_Id(self):
        return self.__id

    def set_Id(self, id):
        self.__id = id

    def get_salario_base(self):
        return self.__salario_base

    def set_salario_base(self, salario_base):
        self.__salario_base = salario_base
