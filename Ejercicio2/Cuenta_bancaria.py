class cuenta_bancaria:
    def __init__(self, Num_cuenta, Titular, Saldo, Fecha_apertura):
        self.__Num_cuenta = Num_cuenta
        self.__Titular = Titular
        self.__Saldo = Saldo
        self.__Fecha_apertura = Fecha_apertura
    
    def get_Num_cuenta(self):
        return self.__Num_cuenta
    
    def set_Titular(self, nuevo_Titular):
        self.__Titular = nuevo_Titular
    def get_Titular(self):
        return self.__Titular
    
    def set_Saldo(self, nuevo_Saldo):
        self.__Saldo = nuevo_Saldo
    def get_Saldo(self):
        return self.__Saldo
    
    def set_Fecha_apertura(self, nuevo_Fecha_apertura):
        self.__Fecha_apertura = nuevo_Fecha_apertura
    def get_Fecha_apertura(self):
        return self.__Fecha_apertura
    
    def depositar(self, monto):
        if monto > 0:
            self.__Saldo += monto
            print(f"Deposito exitoso. Nuevo saldo: ${self.__Saldo}")
        else: 
            print("Error: El monto depositado debe ser mayor a 0")

    def retirar(self, monto):
        if monto <= 0:
            print("Error el monto a retirar debe ser mayor a 0")
        elif monto > self.__Saldo:
            print(f"Error: saldo insuficiente. saldo disponible: ${self.__Saldo}")
        else:
            self.__Saldo -= monto
            print(f"Retiro exitoso. Nuevo saldo: ${self.__Saldo}")
    

