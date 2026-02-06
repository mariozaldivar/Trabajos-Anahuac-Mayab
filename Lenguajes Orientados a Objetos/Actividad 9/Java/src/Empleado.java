public class Empleado {

    String toString(int n)
    {
        return Integer.toString(n);
    }
    // Propiedades, setters y getters
    private String nombre;
    public String getNombre()
    {
        return nombre;
    }
    public void getNombre(String newname)
    {
        this.nombre = newname;
    }

    private int anioContratacion;
    public int getAnioContratacion()
    {
        return anioContratacion;
    }
    public void setAnioContratacion(int a)
    {
        this.anioContratacion = a;
    }

    private double salario;
    public double getSalario()
    {
        return salario;
    }
    public void setSalario(double s)
    {
        this.salario = s;
    }


    // Constructores
    public Empleado()
    {
        this.nombre = "NULL";
        this.anioContratacion = 0;
        this.salario = 0.0;

    }

    Empleado(String n, int anio, double s)
    {
        this.nombre = n;
        this.anioContratacion = anio;
        this.salario = s;

    }

    // Métodos
    public void Imprimir()
    {
        System.out.println("Nombre: " + this.nombre);
        System.out.println("Año de contratación: " + this.anioContratacion);
        System.out.println("Salario: " + this.salario);
    }

    public double CalcularSalario()
    {
        double salario_mensual = this.salario*12;

        System.out.println("Teniendo en cuenta que el salario introducido es mensual, su salario anualmente es de $" + salario_mensual);
        return salario_mensual;
    }

}
