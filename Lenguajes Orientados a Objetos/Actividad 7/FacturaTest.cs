using System;

class Program
{
    public static int Main()
    {

        Console.WriteLine("Introduzca el numero de la pieza: ");
        string num = Console.ReadLine();
        Console.WriteLine("Introduzca una descripcion para la pieza: ");
        string desc = Console.ReadLine();
        Console.WriteLine("Introduzca la cantidad del producto: ");
        int cantidad = int.Parse(Console.ReadLine());
        Console.WriteLine("Introduzca el precio del producto: ");
        double precio = double.Parse(Console.ReadLine());

        // Por como está programado, todos los atributos se pueden declarar en la contrucicón del objeto 
        Factura factura = new Factura(num, desc, cantidad, precio);


        Console.WriteLine("El precio total de la factura es: $" + factura.ObtenerMontoFactura());
        return 1;
    }
}