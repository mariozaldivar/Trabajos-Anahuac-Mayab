class Empleado:
    def __init__(self, nombre, apellido, nss):
        self._primer_nombre = nombre
        self._apellido_paterno = apellido
        self._numero_seguro_social = nss

    @property
    def primer_nombre(self):
        return self._primer_nombre

    @primer_nombre.setter
    def primer_nombre(self, nombre):
        self._primer_nombre = nombre

    @property
    def apellido_paterno(self):
        return self._apellido_paterno

    @apellido_paterno.setter
    def apellido_paterno(self, apellido):
        self._apellido_paterno = apellido

    @property
    def numero_seguro_social(self):
        return self._numero_seguro_social

    @numero_seguro_social.setter
    def numero_seguro_social(self, nss):
        self._numero_seguro_social = nss

    def ingresos(self):
        raise NotImplementedError(
            "Subclase debe implementar el método ingresos")

    def __str__(self):
        return f"{self.primer_nombre} {self.apellido_paterno}\nnumero de seguro social: {self.numero_seguro_social}"
