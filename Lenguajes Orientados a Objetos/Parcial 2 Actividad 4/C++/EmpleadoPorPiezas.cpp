#include "EmpleadoPorPiezas.h"

EmpleadoPorPiezas::EmpleadoPorPiezas(string n, string a, string nss, double s, double p)
    : Empleado(n, a, nss) {
    establecerSueldo(s);
    establecerPiezas(p);
}

void EmpleadoPorPiezas::establecerSueldo(double s) { sueldo = (s < 0.0) ? 0.0 : s; }
void EmpleadoPorPiezas::establecerPiezas(double p) { piezas = (p < 0.0) ? 0.0 : p; }

double EmpleadoPorPiezas::ingresos() const { return sueldo * piezas; }

void EmpleadoPorPiezas::imprimir() const {
    cout << "empleado por piezas: ";
    Empleado::imprimir();
    cout << "\nsueldo por pieza: $" << sueldo << "; piezas vendidas: " << piezas;
}
