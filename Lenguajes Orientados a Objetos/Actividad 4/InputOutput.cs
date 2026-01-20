// Mario Andrés Zaldívar de la Cruz
// #00586553

using System;
class InputOutput
{
    static void Main()
    {
        
        string nombre;
        int n1, n2;

        Console.WriteLine("¿Cuál es tu nombre?");
        nombre = Console.ReadLine();

        Console.WriteLine("Hola " + nombre + ", escribe dos valores enteros: ");
        n1 = int.Parse(Console.ReadLine());
        n2 = int.Parse(Console.ReadLine());

    }
}