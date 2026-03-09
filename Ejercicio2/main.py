from Cuenta_bancaria import cuenta_bancaria

cuenta1 = cuenta_bancaria("001", "Juan Gomez", 1000, "2024-01-15")
cuenta2 = cuenta_bancaria("004", "Anna perez", 500, "2021-05-25")

print("======== CUENTAS CREADAS ========")
print(f"Cuenta: {cuenta1.get_Num_cuenta()} | Titular: {cuenta1.get_Titular()} | Saldo: ${cuenta1.get_Saldo()}")
print(f"Cuenta: {cuenta2.get_Num_cuenta()} | Titular: {cuenta2.get_Titular()} | Saldo: ${cuenta2.get_Saldo()}")

print("==== OPERACIONES CUENTA 1 =======")
cuenta1.depositar(500)
cuenta1.retirar(200)
cuenta1.retirar(2000)
cuenta1.depositar(-1000)

print("==== OPERACIONES CUENTA 2 =======")
cuenta2.depositar(300)
cuenta2.retirar(100)

print("==== SALDOS FINALES =======")
print(f"{cuenta1.get_Titular()}: ${cuenta1.get_Saldo()}")
print(f"{cuenta2.get_Titular()}: ${cuenta2.get_Saldo()}")


