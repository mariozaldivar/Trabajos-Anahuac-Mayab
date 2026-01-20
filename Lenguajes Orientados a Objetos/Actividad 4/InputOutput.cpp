#include <iostream>
#include <string>

using namespace std;

int main()
{
    string nombre;
    float num1;
    float num2;

    cout << "Introduce tu nombre :)" << endl;
    cin >> nombre;
    cout << "Introduce dos numeros para sumar" << endl;
    cin >> num1;
    cout << endl;
    cin >> num2;

    cout << endl << "La suma de ambos numeros es " << num1+num2 << endl;


}