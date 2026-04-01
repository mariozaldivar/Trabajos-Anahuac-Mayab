#ifndef EMPLEADO_H
#define EMPLEADO_H

#include <iostream>
#include <string>

using namespace std;

class Empleado {
protected:
    string primerNombre;
    string apellidoPaterno;
    string numeroSeguroSocial;

public:
    Empleado(string, string, string);
    virtual ~Empleado();

    void establecerPrimerNombre(string);
    string obtenerPrimerNombre() const;

    void establecerApellidoPaterno(string);
    string obtenerApellidoPaterno() const;

    void establecerNumeroSeguroSocial(string);
    string obtenerNumeroSeguroSocial() const;

    virtual double ingresos() const = 0; 
    virtual void imprimir() const;
};

#endif
