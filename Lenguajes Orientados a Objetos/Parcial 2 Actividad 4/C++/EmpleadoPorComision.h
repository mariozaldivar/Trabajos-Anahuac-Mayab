#ifndef EMPLEADOPORCOMISION_H
#define EMPLEADOPORCOMISION_H

#include "Empleado.h"

using namespace std;

class EmpleadoPorComision : public Empleado {
protected: 
    double ventasBrutas;
    double tarifaComision;

public:
    EmpleadoPorComision(string, string, string, double, double);
    void establecerVentasBrutas(double);
    double obtenerVentasBrutas() const;
    void establecerTarifaComision(double);
    double obtenerTarifaComision() const;
    virtual double ingresos() const override;
    virtual void imprimir() const override;
};

#endif
