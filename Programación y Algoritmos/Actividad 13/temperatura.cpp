#include <iostream>
#include <string>
#include <iomanip>

using namespace std;

float fahrenheit;
float celsius;
string mensaje;

int main() 
{
    cout << "Introduzca la temperatura en grados Fahrenheit" << endl;
    cin >> fahrenheit;
    celsius = (fahrenheit - 32) * 5/9;
    cout << "La temperatura dada equivale a " << setprecision(4) << celsius << " grados Celsius" << endl;

    if (celsius >= 20 && celsius <= 25)
    {
        mensaje = "ideal";
    }
    else if (celsius < 20)
    {
        mensaje = "no clasificada";
    }
    else if (celsius > 25 && celsius <= 32)
    {
        mensaje = "peligrosa";
    }
    else if (celsius > 32)
    {
        mensaje = "contraindicada";
    }

    cout << "Esta temperatura es " << mensaje << endl;
    

}