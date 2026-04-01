from Empleado import Empleado


class EmpleadoPorPiezas(Empleado):
    def __init__(self, nombre, apellido, nss, sueldo_por_pieza, piezas_vendidas):
        super().__init__(nombre, apellido, nss)
        self.sueldo = sueldo_por_pieza
        self.piezas = piezas_vendidas

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
    def piezas(self):
        return self._piezas

    @piezas.setter
    def piezas(self, valor):
        if valor < 0.0:
            self._piezas = 0.0
        else:
            self._piezas = valor

    def ingresos(self):
        return self.sueldo * self.piezas

    def __str__(self):
        return f"empleado por piezas: {super().__str__()}\nsueldo por pieza: ${self.sueldo:,.2f}; piezas vendidas: {self.piezas:,.2f}"
