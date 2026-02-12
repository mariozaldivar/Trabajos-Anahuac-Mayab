// Mario Andrés Zaldívar de la Cruz
// ID: 00586553

using System;

class PruebaCuenta
{
    public static void Main()
    {
        Cuenta cuenta1 = new Cuenta("John Green", 50.00);
        Cuenta cuenta2 = new Cuenta("John Blue", -7.53);
        double monto; 

        Console.WriteLine($"El saldo de la Cuenta 1 es de {cuenta1.Saldo}");
        Console.WriteLine($"El saldo de la Cuenta 2 es de {cuenta2.Saldo}");

        Console.WriteLine("\nIngrese el monto a depositar en la Cuenta 1");
        monto = double.Parse(Console.ReadLine());
        cuenta1.deposito(monto);


        Console.WriteLine($"El saldo de la Cuenta 1 es de {cuenta1.Saldo}");
        Console.WriteLine($"El saldo de la Cuenta 2 es de {cuenta2.Saldo}");


        Console.WriteLine("\nIngrese el monto a depositar en la Cuenta 2");
        monto = double.Parse(Console.ReadLine());
        cuenta2.deposito(monto);



        Console.WriteLine($"El saldo de la Cuenta 1 es de {cuenta1.Saldo}");
        Console.WriteLine($"El saldo de la Cuenta 2 es de {cuenta2.Saldo}");
    }
}