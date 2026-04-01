from EmpleadoPorComision import EmpleadoPorComision


class EmpleadoBaseMasComision(EmpleadoPorComision):
    def __init__(self, nombre, apellido, nss, ventas, tarifa, salario):
        super().__init__(nombre, apellido, nss, ventas, tarifa)
        self.salario_base = salario

    @property
    def salario_base(self):
        return self._salario_base

    @salario_base.setter
    def salario_base(self, valor):
        if valor < 0.0:
            self._salario_base = 0.0
        else:
            self._salario_base = valor

    def ingresos(self):
        return self.salario_base + super().ingresos()

    def __str__(self):
        return f"con salario base {super().__str__()}; salario base: ${self.salario_base:,.2f}"
