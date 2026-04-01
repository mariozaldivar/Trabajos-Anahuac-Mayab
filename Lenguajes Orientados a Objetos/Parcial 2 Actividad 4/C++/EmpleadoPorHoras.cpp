#include "EmpleadoPorHoras.h"

EmpleadoPorHoras::EmpleadoPorHoras(string n, string a, string nss, double s, double h)
    : Empleado(n, a, nss) {
    establecerSueldo(s);
    establecerHoras(h);
}

void EmpleadoPorHoras::establecerSueldo(double s) { sueldo = (s < 0.0) ? 0.0 : s; }
double EmpleadoPorHoras::obtenerSueldo() const { return sueldo; }

void EmpleadoPorHoras::establecerHoras(double h) { horas = (h >= 0.0 && h <= 168.0) ? h : 0.0; }
double EmpleadoPorHoras::obtenerHoras() const { return horas; }

double EmpleadoPorHoras::ingresos() const {
    if (horas <= 40) return sueldo * horas;
    return 40 * sueldo + (horas - 40) * sueldo * 1.5;
}

void EmpleadoPorHoras::imprimir() const {
    cout << "empleado por horas: ";
    Empleado::imprimir();
    cout << "\nsueldo por hora: $" << sueldo << "; horas trabajadas: " << horas;
}
