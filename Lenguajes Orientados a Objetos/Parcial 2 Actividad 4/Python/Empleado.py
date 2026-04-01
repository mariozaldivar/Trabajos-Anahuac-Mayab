from abc import ABC, abstractmethod


class Empleado(ABC):

    def __init__(self, nombre, apellido, nss):
        self._primerNombre = nombre
        self._apellidoPaterno = apellido
        self._numeroSeguroSocial = nss

    @property
    def primerNombre(self):
        return self._primerNombre

    @primerNombre.setter
    def primerNombre(self, nombre):
        self._primerNombre = nombre

    @property
    def apellidoPaterno(self):
        return self._apellidoPaterno

    @apellidoPaterno.setter
    def primerNombre(self, apellido):
        self._apellidoPaterno = apellido

    @property
    def numeroSeguroSocial(self):
        return self._numeroSeguroSocial

    @numeroSeguroSocial.setter
    def numeroSeguroSocial(self, nss):
        self._numeroSeguroSocial = nss

    @abstractmethod
    def ingresos(self):
        pass
