#include "EmpleadoPorComision.h"

EmpleadoPorComision::EmpleadoPorComision(string n, string a, string nss, double v, double t)
    : Empleado(n, a, nss) {
    establecerVentasBrutas(v);
    establecerTarifaComision(t);
}

void EmpleadoPorComision::establecerVentasBrutas(double v) { ventasBrutas = (v < 0.0) ? 0.0 : v; }
double EmpleadoPorComision::obtenerVentasBrutas() const { return ventasBrutas; }

void EmpleadoPorComision::establecerTarifaComision(double t) { tarifaComision = (t > 0.0 && t < 1.0) ? t : 0.0; }
double EmpleadoPorComision::obtenerTarifaComision() const { return tarifaComision; }

double EmpleadoPorComision::ingresos() const { return tarifaComision * ventasBrutas; }

void EmpleadoPorComision::imprimir() const {
    cout << "empleado por comision: ";
    Empleado::imprimir();
    cout << "\nventas brutas: $" << ventasBrutas << "; tarifa de comision: " << tarifaComision;
}
