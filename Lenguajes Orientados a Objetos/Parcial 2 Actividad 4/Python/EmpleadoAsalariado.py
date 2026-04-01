from Empleado import Empleado


class EmpleadoAsalariado(Empleado):

    def __init__(self, nombre, apellido, nss, salario):
        super().__init__(nombre, apellido, nss)
        self._salario_semanal = salario

    @property
    def salario_semanal(self):
        return self._salario_semanal

    @salario_semanal.setter
    def salario_semanal(self, salario):
        self._salario_semanal = salario

    def ingresos(self):
        return self._salario_semanal
