using System;

public class Cuenta
{
    private string nombre;

    private double saldo; 

    public string Nombre{
        set { nombre = value;}
        get { return nombre;} 
    }
    public double Saldo
    {
        set {saldo = value;} 
        get {return saldo;}  
    }

    void deposito(double monto_deposito)
    {
        if (monto_deposito > 0.0)
        {
            saldo += monto_deposito; 
            Console.WriteLine($"Se ha depositado el monto de ${monto_deposito}, ahora el saldo total es de ${saldo}");
        }

    }


}