import java.util.Scanner;

public class testEmpleado {

    public static void main(String[] args)
    {
        Empleado empl_void = new Empleado();
        empl_void.Imprimir();

        Empleado empl = new Empleado("Donald Trump", 2025, 10000);
        empl.Imprimir();

        String nombre;
        int anio;
        double sal;

        Scanner scanner = new Scanner(System.in);
        System.out.println("Introduzca el nombre del empleado: ");
        nombre = scanner.nextLine();
        System.out.println("Introduzca el año en el que fue contratado: ");
        anio = scanner.nextInt();
        System.out.println("Introduzca el salario mensual: ");
        sal = scanner.nextDouble();


        Empleado empl_manual = new Empleado(nombre, anio, sal);

        empl_manual.Imprimir();
        empl_manual.CalcularSalario();


    }
}
