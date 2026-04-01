from Empleado import Empleado


class EmpleadoPorHoras(Empleado):
    def __init__(self, nombre, apellido, nss, sueldo_por_horas, horas_trabajadas):
        super().__init__(nombre, apellido, nss)
        self.sueldo = sueldo_por_horas
        self.horas = horas_trabajadas

    @property
    def sueldo(self):
        return self._sueldo

    @sueldo.setter
    def sueldo(self, valor):
        if valor < 0.0:
            self._sueldo = 0.0
        else:
            self._sueldo = valor

    @property
    def horas(self):
        return self._horas

    @horas.setter
    def horas(self, valor):
        if 0.0 <= valor <= 168.0:
            self._horas = valor
        else:
            self._horas = 0.0

    def ingresos(self):
        if self.horas <= 40:
            return self.sueldo * self.horas
        else:
            return 40 * self.sueldo + (self.horas - 40) * self.sueldo * 1.5

    def __str__(self):
        return f"empleado por horas: {super().__str__()}\nsueldo por hora: ${self.sueldo:,.2f}; horas trabajadas: {self.horas:,.2f}"
