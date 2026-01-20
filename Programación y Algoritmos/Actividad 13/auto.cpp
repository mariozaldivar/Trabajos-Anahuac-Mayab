#include <iostream>
#include <string>

using namespace std;

float tarifa;
float kilometros;

int main() 
{
    tarifa = 850;
    cout << "Introduzca la cantidad de kilometros recorridos" << endl;
    cin >> kilometros;
    
    if (kilometros > 200)
    {
        tarifa = tarifa + (4.50 * (kilometros - 200));
    }

    cout << "Monto a pagar: $" << tarifa << endl;
    cout << "IVA: $" << tarifa*.16 << endl;
    cout << "Monto total: $" << tarifa*1.16 << endl;
}