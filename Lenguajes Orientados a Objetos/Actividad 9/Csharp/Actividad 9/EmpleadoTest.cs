using System;

class EmpleadoTest
{
    public static void Main()
    {
        Empleado empl = new Empleado("Donald Trump", 2025, 10000);
        empl.Imprimir();
        empl.CalcularSalario();

        Empleado empl_void = new Empleado();

        empl_void.Imprimir();
    }
}