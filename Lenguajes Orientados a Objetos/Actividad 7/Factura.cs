using System;

class Factura
{
    public string Numero_pieza;
    public string Descripcion_pieza;
    public int Cantidad;
    public double Precio;


    public Factura(string numero_pieza, string descripcion_pieza, int cantidad, double precio)
    {
        Numero_pieza = numero_pieza;
        Descripcion_pieza =  descripcion_pieza;
        if (cantidad < 0)
        {
            Cantidad = 0;
        }
        else
        {
            Cantidad = cantidad;
        }


        if (precio < 0)
        {
            Precio = 0.0;
        }
        else
        {
            Precio = precio;
        }
    }

    public double ObtenerMontoFactura()
    {
        double total = Cantidad * Precio;

        return total;
    }
}