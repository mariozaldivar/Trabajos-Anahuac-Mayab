#include <iostream>
#include <iomanip>
#include <vector>
#include "EmpleadoAsalariado.h"
#include "EmpleadoPorHoras.h"
#include "EmpleadoPorComision.h"
#include "EmpleadoBaseMasComision.h"
#include "EmpleadoPorPiezas.h"

using namespace std;

// Función que recibe referencia para ejecutar polimorfismo
void mostrarDatos(Empleado& e) {
    e.imprimir();
    cout << "\ningresos: $" << e.ingresos() << "\n\n";
}

int main() {
    cout << fixed << setprecision(2);

    EmpleadoAsalariado e1("John", "Smith", "111-11-1111", 800.00);
    EmpleadoPorHoras e2("Karen", "Price", "222-22-2222", 16.75, 40);
    EmpleadoPorComision e3("Sue", "Jones", "333-33-3333", 10000, 0.06);
    EmpleadoBaseMasComision e4("Bob", "Lewis", "444-44-4444", 5000, 0.04, 300);
    EmpleadoPorPiezas e5("Mario", "Gomez", "555-55-5555", 25.50, 100);

    cout << "Sistema de Nomina procesado por referencias:\n\n";

    mostrarDatos(e1);
    mostrarDatos(e2);
    mostrarDatos(e3);
    
    // Ejemplo de manipulación antes de imprimir
    double baseAnterior = e4.obtenerSalarioBase();
    e4.establecerSalarioBase(baseAnterior * 1.10); // 10% aumento
    mostrarDatos(e4);
    
    mostrarDatos(e5);

    return 0;
}
