#include <iostream>
#include <cmath>


using namespace std;

float CalcularIMC(float peso, float estatura);
void ImprimirEstadoDeSalud(float imc);

int main()
{
    float peso;
    float estatura;

    cout << "Introduzca el peso en kg y la estatura en metros de la persona cuyo IMC quiera calcular: " << endl;
    cin >> peso;
    cin >> estatura;
    cout << endl; 
    float imc = CalcularIMC(peso, estatura);

    cout << "El IMC de esta persona es " << imc << endl;
    cout << endl << "El peso de esta persona corresponde a: "; 

    ImprimirEstadoDeSalud(imc);
    cout << endl;
}


float CalcularIMC(float peso, float estatura)
{
    float imc = peso/(pow(estatura,2));

    return imc;
}

void ImprimirEstadoDeSalud(float imc)
{
    if (imc < 18)
    {
        cout << "Peso bajo" << endl; 
    }
    else if (imc >= 18 && imc < 25)
    {
        cout << "Peso normal" << endl; 
    }
    else if (imc >= 25 && imc < 27)
    {
        cout << "Sobrepeso" << endl;
    }
    else if (imc >= 27 && imc < 30)
    {
        cout << "Obesidad grado I" << endl;
    }
    else if (imc >= 30 && imc < 40)
    {
        cout << "Obesidad grado II" << endl;
    }
    else 
    {
        cout << "Obesidad grado III" << endl;
    }
}

