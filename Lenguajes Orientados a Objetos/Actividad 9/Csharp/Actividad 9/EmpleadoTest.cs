using System;

class EmpleadoTest
{
    public static void Main()
    {
        Empleado empl_void = new Empleado();

        empl_void.Imprimir();


        Empleado empl = new Empleado("Donald Trump", 2025, 10000);
        empl.Imprimir();


        string nombre; 
        int anio;
        double sal;

        Console.WriteLine("Introduzca el nombre del empleado: ");
        nombre = Console.ReadLine();
        Console.WriteLine("Introduzca el año en el que fue contratado: ");
        anio = Convert.ToInt32(Console.ReadLine());
        Console.WriteLine("Introduzca el salario mensual: $");
        sal = Convert.ToDouble(Console.ReadLine());


        Empleado empl_manual = new Empleado(nombre, anio, sal);

        empl_manual.Imprimir();


    }
}