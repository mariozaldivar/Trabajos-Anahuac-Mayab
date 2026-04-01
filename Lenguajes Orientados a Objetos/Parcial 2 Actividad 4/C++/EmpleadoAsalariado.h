#ifndef EMPLEADOASALARIADO_H
#define EMPLEADOASALARIADO_H

#include "Empleado.h"

class EmpleadoAsalariado : public Empleado {
private:
    double salarioSemanal;

public:
    EmpleadoAsalariado(string, string, string, double);
    void establecerSalarioSemanal(double);
    double obtenerSalarioSemanal() const;
    virtual double ingresos() const override;
    virtual void imprimir() const override;
};

#endif
