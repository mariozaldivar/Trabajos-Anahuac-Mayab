from EmpleadoAsalariado import EmpleadoAsalariado
from EmpleadoPorHoras import EmpleadoPorHoras
from EmpleadoPorComision import EmpleadoPorComision
from EmpleadoBaseMasComision import EmpleadoBaseMasComision
from EmpleadoPorPiezas import EmpleadoPorPiezas

# Creación de objetos originales
empleado_asalariado = EmpleadoAsalariado(
    "John", "Smith", "111-11-1111", 800.00)
empleado_por_horas = EmpleadoPorHoras(
    "Karen", "Price", "222-22-2222", 16.75, 40)
empleado_por_comision = EmpleadoPorComision(
    "Sue", "Jones", "333-33-3333", 10000, 0.06)
empleado_base_mas_comision = EmpleadoBaseMasComision(
    "Bob", "Lewis", "444-44-4444", 5000, 0.04, 300)

# Nuevo objeto basado en el UML
empleado_por_piezas = EmpleadoPorPiezas(
    "Mario", "Gomez", "555-55-5555", 25.50, 100)

print("Empleados procesados por separado:\n")

lista_individual = [
    empleado_asalariado,
    empleado_por_horas,
    empleado_por_comision,
    empleado_base_mas_comision,
    empleado_por_piezas
]

for e in lista_individual:
    print(f"{e}\ningresos: ${e.ingresos():,.2f}\n")

# Lista para procesamiento polimórfico
empleados = [
    empleado_asalariado,
    empleado_por_horas,
    empleado_por_comision,
    empleado_base_mas_comision,
    empleado_por_piezas
]

print("Empleados procesados en forma polimorfica:\n")

for empleado_actual in empleados:
    print(empleado_actual)

    # Caso especial para EmpleadoBaseMasComision
    if isinstance(empleado_actual, EmpleadoBaseMasComision):
        salario_anterior = empleado_actual.salario_base
        empleado_actual.salario_base = 1.10 * salario_anterior
        print(f"el nuevo salario base con 10% de aumento es: ${
              empleado_actual.salario_base:,.2f}")

    print(f"ingresos ${empleado_actual.ingresos():,.2f}\n")

# Mostrar tipos de clase
for i, empleado in enumerate(empleados):
    print(f"El empleado {i} es un {empleado.__class__.__name__}")
