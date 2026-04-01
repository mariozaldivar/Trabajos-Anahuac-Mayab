#include "Empleado.h"

Empleado::Empleado(string nombre, string apellido, string nss) 
    : primerNombre(nombre), apellidoPaterno(apellido), numeroSeguroSocial(nss) {}

Empleado::~Empleado() {}

void Empleado::establecerPrimerNombre(string nombre) { primerNombre = nombre; }
string Empleado::obtenerPrimerNombre() const { return primerNombre; }

void Empleado::establecerApellidoPaterno(string apellido) { apellidoPaterno = apellido; }
string Empleado::obtenerApellidoPaterno() const { return apellidoPaterno; }

void Empleado::establecerNumeroSeguroSocial(string nss) { numeroSeguroSocial = nss; }
string Empleado::obtenerNumeroSeguroSocial() const { return numeroSeguroSocial; }

void Empleado::imprimir() const {
    cout << primerNombre << " " << apellidoPaterno 
         << "\nnumero de seguro social: " << numeroSeguroSocial;
}
