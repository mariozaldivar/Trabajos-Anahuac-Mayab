from Empleado import Empleado


class EmpleadoPorComision(Empleado):
    def __init__(self, nombre, apellido, nss, ventas, tarifa):
        super().__init__(nombre, apellido, nss)
        self.ventas_brutas = ventas
        self.tarifa_comision = tarifa

    @property
    def ventas_brutas(self):
        return self._ventas_brutas

    @ventas_brutas.setter
    def ventas_brutas(self, valor):
        if valor < 0.0:
            self._ventas_brutas = 0.0
        else:
            self._ventas_brutas = valor

    @property
    def tarifa_comision(self):
        return self._tarifa_comision

    @tarifa_comision.setter
    def tarifa_comision(self, valor):
        if 0.0 < valor < 1.0:
            self._tarifa_comision = valor
        else:
            self._tarifa_comision = 0.0

    def ingresos(self):
        return self.tarifa_comision * self.ventas_brutas

    def __str__(self):
        return f"empleado por comision: {super().__str__()}\nventas brutas: ${self.ventas_brutas:,.2f}; tarifa de comision: {self.tarifa_comision:.2f}"
