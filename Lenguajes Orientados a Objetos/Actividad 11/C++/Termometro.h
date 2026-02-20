#pragma once 
#include <string> 
#include <iostream>
#include <random>
#include <ctime>

using namespace std;

class Termometro
{
    public :
    float tempC; 
    

    Termometro()
    {
        srand(time(NULL));
        tempC = rand() % 100;
    }

    Termometro(float temp)
    {
        tempC = temp;
    }


    float TemperaturaC()
    {
        cout << "La temperatura en °C es de: " << tempC << "°C" << endl;
        return tempC;
    }
    float TemperaturaK()
    {
        float tempK = tempC + 273.15;
        cout << "La temperatura en K es de: " << tempK << "K" << endl;
        return tempK;
    }
    float TemperaturaF()
    {
        float tempF = (tempC * 9/5) + 32;
        cout << "La temperatura en °F es de: " << tempF << "°F" << endl;
        return tempC;
    }

    void MostrarTemperatura()
    {
        TemperaturaC();
        TemperaturaF();
        TemperaturaK();
    }


};
