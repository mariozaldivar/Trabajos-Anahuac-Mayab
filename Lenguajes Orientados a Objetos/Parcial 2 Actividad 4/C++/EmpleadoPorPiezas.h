#ifndef EMPLEADOPORPIEZAS_H
#define EMPLEADOPORPIEZAS_H

#include "Empleado.h"

class EmpleadoPorPiezas : public Empleado {
private:
    double sueldo;
    double piezas;

public:
    EmpleadoPorPiezas(string, string, string, double, double);
    void establecerSueldo(double);
    void establecerPiezas(double);
    virtual double ingresos() const override;
    virtual void imprimir() const override;
};

#endif
