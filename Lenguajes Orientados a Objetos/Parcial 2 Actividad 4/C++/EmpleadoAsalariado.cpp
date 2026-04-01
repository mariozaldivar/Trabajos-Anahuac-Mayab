#include "EmpleadoAsalariado.h"

EmpleadoAsalariado::EmpleadoAsalariado(string n, string a, string nss, double s)
    : Empleado(n, a, nss) {
    establecerSalarioSemanal(s);
}

void EmpleadoAsalariado::establecerSalarioSemanal(double s) {
    salarioSemanal = (s < 0.0) ? 0.0 : s;
}

double EmpleadoAsalariado::obtenerSalarioSemanal() const { return salarioSemanal; }

double EmpleadoAsalariado::ingresos() const { return obtenerSalarioSemanal(); }

void EmpleadoAsalariado::imprimir() const {
    cout << "empleado asalariado: ";
    Empleado::imprimir();
    cout << "\nsalario semanal: $" << salarioSemanal;
}
