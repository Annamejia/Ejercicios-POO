from Curso import Curso
class Estudiante:
    def __init__(self, id, nombre, codigo_estudiantil, carrera):
        self.__id = id
        self.__nombre = nombre
        self.__codigo_estudiantil = codigo_estudiantil
        self.__carrera = carrera
        self.__curso = []
    
    def get_id(self):
        return self.__id
    
    def set_nombre(self, nuevo_nombre):
        self.__nombre = nuevo_nombre
    def get_nombre(self):
        return self.__nombre
    
    def set_codigo_estudiantil(self, nuevo_cogigo_estudiantil):
        self.__codigo_estudiantil = nuevo_cogigo_estudiantil
    def get_codigo_estudiantil(self):
        return self.__codigo_estudiantil
    
    def set_carrera(self, nueva_carrera):
        self.__carrera = nueva_carrera
    def get_carrera(self):
        return self.__carrera
    
    def Matricular(self, curso):
        if isinstance(curso, Curso):
            self.__curso.append(curso)
            print(f"{self.__nombre} matriculado en: {curso.get_nombre()}")
        else:
            print("Error: el objeto no es un Curso válido.")

    def get_curso(self):
        return self.__curso

    def __str__(self):
        return (f"Estudiante: {self.__nombre} | "
                f"Código: {self.__codigo_estudiantil} | "
                f"Carrera: {self.__carrera}")


    

    
    
