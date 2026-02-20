#include "Termometro.h"
#include <iostream>
using namespace std;

int main()
{
    Termometro termometro1;
    Termometro termometro2(30);
    cout << "Para el termometro 1: ";
    termometro1.MostrarTemperatura();
    cout << endl;
    cout << "Para el termometro 2:";
    termometro2.MostrarTemperatura();
}
