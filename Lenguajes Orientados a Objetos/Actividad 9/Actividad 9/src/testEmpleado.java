public class testEmpleado {

    public static void main(String[] args)
    {
        Empleado empl = new Empleado("Donald Trump", 2025, 20000);
        empl.Imprimir();
        empl.CalcularSalario();

        Empleado voidempl = new Empleado();

        voidempl.Imprimir();
    }
}
