#ifndef EMPLEADOPORHORAS_H
#define EMPLEADOPORHORAS_H

#include "Empleado.h"

using namespace std;

class EmpleadoPorHoras : public Empleado {
private:
    double sueldo;
    double horas;

public:
    EmpleadoPorHoras(string, string, string, double, double);
    void establecerSueldo(double);
    double obtenerSueldo() const;
    void establecerHoras(double);
    double obtenerHoras() const;
    virtual double ingresos() const override;
    virtual void imprimir() const override;
};

#endif
