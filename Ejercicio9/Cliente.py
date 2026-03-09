class Cliente:
    def __init__(self, nombre, email, telefono):
        self.__nombre = nombre
        self.__email = email
        self.__telefono = telefono

   
    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        self.__nombre = nombre

  
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

   
    def get_telefono(self):
        return self.__telefono

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def __str__(self):
        return (f"Cliente: {self.__nombre} | "
                f"Email: {self.__email} | "
                f"Teléfono: {self.__telefono}")