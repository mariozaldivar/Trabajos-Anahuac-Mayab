// Mario Andrés Zaldívar de la Cruz
// ID: 00586553

#include <iostream>
#include <iomanip>

using namespace std;

int MayoresQue30( float partidos[])
{
    int contador = 0;
    for (int i = 0; i < 7; i++) 
    {
        if (partidos[i] > 30)
        {
            contador++;
        }

    }
    return contador; 
    
}
float Promedio(float partidos[])
{
    float suma = 0; 
    for (int i = 0; i < 7; i++)
    {
        suma = suma + partidos[i];
    }
    return suma/7;
}

void MayorPartido(float partidos[])
{
    float max = 0;
    for (int i = 0; i < 7; i++)
    {
        if (partidos[i] > max)
        {
            max = partidos[i];
        }
        
    }
    cout << "Su mayor cantidad de puntos anotados en un partido fue de " << max << " puntos" << endl; 
    cout << "Su porcentaje de puntos por tiro libre fue " << (15/max) * 100 << "%" << endl << endl;
}

int main() 
{
    float partidos[7];
    for (int i = 0; i < 7; i++)
    {
        int partido;
        cout << "Introduzca el puntaje en el partido " << i << ": ";
        cin >> partido; 
        partidos[i] = partido; 
        
    }

    cout << endl; 
    cout << "Su puntaje promedio por partido fue de " << Promedio(partidos) << endl; 
    cout << "El jugador tuvo " << MayoresQue30(partidos) << " partidos con mas de 30 puntos" << endl; 
    MayorPartido(partidos);

    
}