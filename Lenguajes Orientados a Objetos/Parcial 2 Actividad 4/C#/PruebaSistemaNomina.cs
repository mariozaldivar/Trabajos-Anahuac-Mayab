using System;
using System.Collections.Generic;

namespace SistemaNomina
{
    class PruebaSistemaNomina
    {
        static void Main(string[] args)
        {
            var e1 = new EmpleadoAsalariado("John", "Smith", "111-11-1111", 800.00m);
            var e2 = new EmpleadoPorHoras("Karen", "Price", "222-22-2222", 16.75m, 40);
            var e3 = new EmpleadoPorComision("Sue", "Jones", "333-33-3333", 10000m, 0.06);
            var e4 = new EmpleadoBaseMasComision("Bob", "Lewis", "444-44-4444", 5000m, 0.04, 300m);
            var e5 = new EmpleadoPorPiezas("Mario", "Gomez", "555-55-5555", 25.50m, 100);

            List<Empleado> empleados = new List<Empleado> { e1, e2, e3, e4, e5 };

            Console.WriteLine("Empleados procesados polimorficamente:\n");

            foreach (var empleado in empleados)
            {
                Console.WriteLine(empleado);

                // Aumento del 10% si es BaseMasComision
                if (empleado is EmpleadoBaseMasComision empBase)
                {
                    empBase.SalarioBase *= 1.10m;
                    Console.WriteLine($"Nuevo salario base con 10% de aumento: {empBase.SalarioBase:C}");
                }

                Console.WriteLine($"ingresos: {empleado.Ingresos():C}\n");
            }
        }
    }
}



