#ifndef EMPLEADOBASEMASCOMISION_H
#define EMPLEADOBASEMASCOMISION_H

#include "EmpleadoPorComision.h"

using namespace std;

class EmpleadoBaseMasComision : public EmpleadoPorComision {
private:
    double salarioBase;

public:
    EmpleadoBaseMasComision(string, string, string, double, double, double);
    void establecerSalarioBase(double);
    double obtenerSalarioBase() const;
    virtual double ingresos() const override;
    virtual void imprimir() const override;
};

#endif
