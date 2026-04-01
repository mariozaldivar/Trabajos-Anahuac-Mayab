from Empleado import Empleado


class EmpleadoAsalariado(Empleado):
    def __init__(self, nombre, apellido, nss, salario):
        super().__init__(nombre, apellido, nss)
        self.salario_semanal = salario

    @property
    def salario_semanal(self):
        return self._salario_semanal

    @salario_semanal.setter
    def salario_semanal(self, salario):
        if salario < 0.0:
            self._salario_semanal = 0.0
        else:
            self._salario_semanal = salario

    def ingresos(self):
        return self.salario_semanal

    def __str__(self):
        return f"empleado asalariado: {super().__str__()}\nsalario semanal: ${self.salario_semanal:,.2f}"
