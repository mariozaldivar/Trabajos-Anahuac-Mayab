#include "EmpleadoBaseMasComision.h"

EmpleadoBaseMasComision::EmpleadoBaseMasComision(string n, string a, string nss, double v, double t, double s)
    : EmpleadoPorComision(n, a, nss, v, t) {
    establecerSalarioBase(s);
}

void EmpleadoBaseMasComision::establecerSalarioBase(double s) { salarioBase = (s < 0.0) ? 0.0 : s; }
double EmpleadoBaseMasComision::obtenerSalarioBase() const { return salarioBase; }

double EmpleadoBaseMasComision::ingresos() const { 
    return salarioBase + EmpleadoPorComision::ingresos(); 
}

void EmpleadoBaseMasComision::imprimir() const {
    cout << "con salario base ";
    EmpleadoPorComision::imprimir();
    cout << "; salario base: $" << salarioBase;
}



