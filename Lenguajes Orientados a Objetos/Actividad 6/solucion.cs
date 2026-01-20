
using System;
class InputOutput
{
    static void Main()
    {
        /*
        int ni, jo, ad, ma = 0; 
        int pni, pjo, pad, pma = 0; 
         */


        int ni = 0;
        int jo = 0;
        int ad = 0; 
        int ma = 0;
        int pni = 0;
        int pjo = 0;
        int pad = 0;
        int pma = 0; 

        int edad, peso;

        for (int i = 0; i < 5; i++)
        {

            Console.WriteLine("Introduce la edad de la persona " + (i+1));
            edad = int.Parse(Console.ReadLine());

            Console.WriteLine("Introduce el peso de la persona " + (i+1));
            peso = int.Parse(Console.ReadLine());

            if (edad <= 12)
            {
                pni += peso;
                ni++;

            }
            else if (edad <= 29)
            {
                pjo += peso;
                jo++;
            }
            else if (edad <= 59)
            {
                pad += peso;
                ad++;
            }
            else 
            {
                pma += peso;
                ma++;
            }

        }

        Console.WriteLine("Total de niños: " + ni + ", Peso promedio: " + (pni/ni));
        Console.WriteLine("Total de jovenes: " + jo + ", Peso promedio: " + (pjo/jo));
        Console.WriteLine("Total de adultos: " + ad + ", Peso promedio: " + (pad/ad));
        Console.WriteLine("Total de adultos mayores: " + ma + ", Peso promedio: " + (pma/ma));


    }
}