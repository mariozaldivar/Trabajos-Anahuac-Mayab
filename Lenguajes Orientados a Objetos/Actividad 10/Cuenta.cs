using System;

class Cuenta
{
    private string nombre;
    private double saldo; 


    public Cuenta(string name, double sald)
    {
        this.nombre = name;
        if (sald > 0.0 ) {this.saldo = sald;}
        else { this.saldo = 0; }
    }

    public string Nombre{
        set { nombre = value;}
        get { return nombre;} 
    }
    public double Saldo
    {
        set {saldo = value;} 
        get {return saldo;}  
    }

    public void deposito(double monto_deposito)
    {
        if (monto_deposito > 0.0)
        {
            saldo += monto_deposito; 
            Console.WriteLine($"Se ha depositado el monto de ${monto_deposito}, ahora el saldo total es de ${saldo}");
        }

    }


}