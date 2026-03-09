from Empleado import Empleado
from Contratista import Contratista
from EmpleadoFijo import EmpleadoFijo


print("SISTEMA DE GESTIÓN DE EMPLEADOS")

emp1 = EmpleadoFijo("Ana García", 101, 3500.00)
emp2 = EmpleadoFijo("Carlos Martínez", 102, 4200.00)
emp3 = Contratista("Luis Pérez", 103, 0, 25.50, 160)
emp4 = Contratista("María López", 104, 0, 30.00, 120)

empleados = [emp1, emp2, emp3, emp4]

print("\n LISTA DE EMPLEADOS:")
for emp in empleados:
        tipo = "Tiempo Completo" if isinstance(emp, EmpleadoFijo) else "Por Horas"
        print(f"[{tipo}] {emp}")

print("\nACTUALIZANDO DATOS...")
emp3.set_horas_trabajadas(180)
emp4.set_tarifa_Hora(35.00)
emp1.set_salario_base(3800.00)
print("- Luis Pérez: horas actualizadas a 180")
print("- María López: tarifa actualizada a $35.00/hora")
print("- Ana García: salario base actualizado a $3800.00")

print("\n LISTA ACTUALIZADA:")
for emp in empleados:
        tipo = "Tiempo Completo" if isinstance(emp, EmpleadoFijo) else "Por Horas"
        print(f"[{tipo}] {emp}")

total_nomina = sum(emp.Calcular_Salario() for emp in empleados)
print("\n RESUMEN DE NÓMINA:")
print(f"Total empleados    : {len(empleados)}")
print(f"Total a pagar      : ${total_nomina}")

