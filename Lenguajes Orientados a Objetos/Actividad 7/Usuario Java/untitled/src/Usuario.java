public class Usuario {
    String nombre;
    String apellidos;
    int edad;


    void IniciarSesion()
    {
        System.out.println("El usuario " + this.nombre + " está iniciando sesión. ");
    }

    void cerrarSesion()
    {
        System.out.println("El usuario " + this.nombre + " está cerrando su sesión.");
    }

    void hacerReporte()
    {
        System.out.println("Reporte de usuario");
        System.out.println("Nombre completo: " + this.nombre + " " + this.apellidos);
        System.out.println("Edad: " + this.edad);

    }
}
