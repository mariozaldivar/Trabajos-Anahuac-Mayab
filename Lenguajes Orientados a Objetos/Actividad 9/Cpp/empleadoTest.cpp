#include <string>
#include "empleado.h"
#include <iostream>

using namespace std;

int main()
{
    Empleado empl_void;
    empl_void.Imprimir();
    empl_void.calcularSalario();

    Empleado empl("Donald Trump", 2025, 20000);
    empl.Imprimir();
    empl.calcularSalario();


    string nombre;
    int anio;
    double salario;

    cout << "Introduzca el nombre del empleado: ";
    cin >> nombre;
    cout << "\nIntroduzca el anio en que se contrato: ";
    cin >> anio;
    cout << "\n Introduzca el salario mensual de empleado: ";
    cin >> salario;
    cout << endl; 


    Empleado empl_manual(nombre, anio, salario);

    empl_manual.Imprimir();
    empl_manual.calcularSalario();
    

    return 0;
}