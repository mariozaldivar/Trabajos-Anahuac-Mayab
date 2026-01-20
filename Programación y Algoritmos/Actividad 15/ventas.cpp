#include <iostream>
#include <string.h>
using namespace std;

float contador = 0;
float destacadas = 0;
float total = 0;
float venta = 1;
int main()
{

    while (venta > 0)
    {
        cout << "Introduzca el monto de la venta (0 para terminar): ";
        cin >> venta;
        if ( venta > 0  )
        {
            contador++;
            destacadas = (venta > 1000) ? destacadas+1: destacadas;
            total += venta;
        }
        

    }
    string mensaje = "";
    if (total > 5000)
    {
        mensaje = "Excelente jornada de ventas!";
    }
    cout << endl;
    cout << "Ventas totales: " << contador << endl;
    cout << "Monto acumulado: $" << total << "  " << mensaje << endl; 
    cout << "Promedio de venta: $" << total/contador << endl;
    cout << "Ventas destacadas: " << destacadas << endl;

}