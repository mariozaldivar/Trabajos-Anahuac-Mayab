using System;

namespace SistemaNomina
{
    public abstract class Empleado
    {
        public string PrimerNombre { get; set; }
        public string ApellidoPaterno { get; set; }
        public string NumeroSeguroSocial { get; set; }

        public Empleado(string nombre, string apellido, string nss)
        {
            PrimerNombre = nombre;
            ApellidoPaterno = apellido;
            NumeroSeguroSocial = nss;
        }

        // Método abstracto
        public abstract decimal Ingresos();

        public override string ToString()
        {
            return $"{PrimerNombre} {ApellidoPaterno}\nnumero de seguro social: {NumeroSeguroSocial}";
        }
    }
}



