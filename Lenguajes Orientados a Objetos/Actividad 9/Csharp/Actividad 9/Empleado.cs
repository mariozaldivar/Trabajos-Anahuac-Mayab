using System;

public class Empleado
{
    private string nombre;
    private int anioContratacion;
    private double salario;

    public string getNombre()
    {
        return this.nombre;
    }

    public void setNombre(string n)
    {
        this.nombre = n;

    }


    public int getAnioContratacion()
    {
        return this.anioContratacion;
    }

    public void setAnioContratacion(int a)
    {
        this.anioContratacion = a;
    }


    public double getSalario()
    {
        return this.salario;
    }
    public void setSalario(double s)
    {
        this.salario = s;
    }



    public Empleado()
    {
        this.nombre = "NULL";
        this.anioContratacion = 0;
        this.salario = 0.0;

    }

    public Empleado(string n, int a, double s)
    {
        this.nombre = n;
        this.anioContratacion = a;
        this.salario = s;
    }


    
    public void Imprimir()
    {

        Console.WriteLine($"{this.nombre}, contratado desde el {this.anioContratacion}, con salario de ${this.salario}.");
    }

    public double CalcularSalario()
    {
        double anual = salario*12;
        Console.WriteLine($"Tomando en cuenta que el salario mensual es de {this.salario}, el salario anual es de {anual}");
        return anual;
    }




}
