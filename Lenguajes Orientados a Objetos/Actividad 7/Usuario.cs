// Mario Andrés Zaldívar de la Cruz
// #00586553

using System;

class Usuario
{
    public string nombre;
    public string appellidos;
    public int edad;

    void iniciarSesion()
    {
        Console.Writeline("El usuario " + this.nombre + " está iniciando sesión.");

    }

    void cerrarSesion()
    {
        Console.Writeline("El usuario " + this.nombre + " está cerrando sesión.");

    }

    public void hacerReporte()
    {
        Console.WriteLine("Reporte de usuario");
        Console.WriteLine("Nombre completo: " + this.nombre + " " + this.apellidso);
        Console.WriteLine("Edad: " + this.edad);
    }

}
