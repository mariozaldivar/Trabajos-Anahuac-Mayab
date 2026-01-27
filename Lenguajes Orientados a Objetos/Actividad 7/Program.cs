using System;

class Program
{
    public static int Main()
    {
        Factura factura = new Factura("1823u1", "Producto prueba", 20, 35.5);

        Console.WriteLine("El precio es de " + factura.ObtenerMontoFactura());

        return 1;
    }
}