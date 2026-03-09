class Curso: 
    def __init__(self, id, nombre, codigo, num_creditos):
        self.__id = id
        self.__nombre = nombre
        self.__codigo = codigo
        self.__num_creditos = num_creditos
    
    def set_id(self, nuevo_id):
        self.__id = nuevo_id
    def get_id(self):
        return self.__id
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_codigo(self, nuevo_codigo):
        self.__codigo = nuevo_codigo
    def get_codigo(self):
        return self.__codigo
    
    def set_num_creditos(self, nuevo_num_creditos):
        self.__num_creditos = nuevo_num_creditos
    def get_num_creditos(self):
        return self.__num_creditos
    
    def __str__(self):
        return (f"Curso: {self.__nombre} | "
                f"Código: {self.__codigo} | "
                f"Créditos: {self.__num_creditos}")

