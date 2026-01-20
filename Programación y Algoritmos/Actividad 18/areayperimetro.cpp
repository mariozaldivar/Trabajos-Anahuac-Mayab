#define _USE_MATH_DEFINES
#include <iostream>
#include <cmath>

using namespace std;

float CalcularArea(float radio)
{
    return (pow(radio,2)) * M_PI;
}

float CalcularPerimetro(float radio)
{
    return(radio*2*M_PI);
}

int main()
{
    int radio;

    cout << "Introduzca el radio del circulo del cual quiera obtener area y perimetro" << endl; 
    cin >> radio;
    cout << endl; 

    cout << "El area del circulo de radio " << radio << " es de " << CalcularArea(radio) << endl;
    cout << "El perimetro del circulo de radio " << radio << " es de " << CalcularPerimetro(radio) << endl;


    
}

