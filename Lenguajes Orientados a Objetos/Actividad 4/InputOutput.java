/*
Mario Andrés Zaldívar de la Cruz
# 00586553
*/

import java.utilScanner;

class InputOutput
{
    public static void main(String args[])
    {

        Scanner input = new Scanner(System.in);
        String nombre;
        int  n1, n2;

        System.out.println("¿Cuál es tu nombre?");
        nombre = input.nextLine();

        System.out.println("Hola " + nombre + " escribe dos valores enteros");
        n1 = input.nextInt();
        n2 = input.nextInt();



    }
}