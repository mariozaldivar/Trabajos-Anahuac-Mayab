// Mario Andrés Zaldívar de la Cruz
// #00586553

using System;

namespace User
{

class Usuario
{

public string Nombre {get; set;}
public string Apellidos {get; set;}
public int Edad {get; set;}

public Usuario(string nombre, string apellidos, int edad)
{
    Nombre = nombre;
    Apellidos = apellidos;
    Edad = edad;
    
}

void iniciarSesion()
{
    Console.WriteLine("El usuario " + this.nombre + " está iniciando sesión.");

}

void cerrarSesion()
{
    Console.WriteLine("El usuario " + this.nombre + " está cerrando sesión.");

}

public void hacerReporte()
{
    Console.WriteLine("Reporte de usuario");
    Console.WriteLine("Nombre completo: " + this.nombre + " " + this.apellidos);
    Console.WriteLine("Edad: " + this.edad);
}


}

    

}


