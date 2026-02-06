#pragma once
#include <string>
#include <iostream>

using namespace std;


class Empleado
{
    private: 

    string nombre;
    int anioContratacion;
    double salario;

    public: 

    Empleado()
    {
        nombre = "NULL";
        anioContratacion = 0;
        salario = 0.0;
    }


    Empleado(string n, int a, double s)
    {
        nombre = n;
        anioContratacion = a;
        salario = s;
    }

    string getNombre()
    {
        return nombre;
    }
    void setNombre(string n)
    {
        if (nombre != "")
        {
            nombre = n; 
        }
        else 
        {
            nombre = "NULL";
        }
    }

    int getAnioContratacion()
    {
        return anioContratacion;
    }
    void setAnioContratacion(int anio)
    {
        if (anio < 0)
        {
            anioContratacion = anio;
        }
        else 
        {
            anioContratacion = 0; 
        }
    }

    double getSalario()
    {
        return salario;
    }

    void setSalario(double s)
    {
        if (s < 0)
        {
            salario = s;
        }
        else
        {
            salario = 0;
        }
    }

    void Imprimir()
    {
        cout << "El nombre del empleado es: " << nombre << endl;
        cout << "El anio de su contratacion fue: " << anioContratacion << endl;
        cout << "Su salario mensual es de: " << salario << endl; 

    }

    void calcularSalario()
    {
        cout << "Tomando en cuenta que el salario mensual es de " << salario << ", el salario anual de este empleado es de $" << salario*12.0 << "." << endl;
    }
    
};