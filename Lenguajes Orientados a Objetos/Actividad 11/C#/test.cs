using System;

class Test
{
    public static void Main()
    {
        Termometro termometro1 = new Termometro(30);
    
        Termometro termometro2 = new Termometro();
        Console.WriteLine("Para el termometro parametrizado: ");
        termometro1.MostrarTemperatura();
        Console.WriteLine("Para el termometro sin parametrizar: ");
        termometro2.MostrarTemperatura();
    }
}
