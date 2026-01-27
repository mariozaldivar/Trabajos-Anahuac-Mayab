//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.


void main() {
  Usuario user = new Usuario();
  user.nombre = "Mario Andrés";
  user.apellidos = "Zaldívar de la Cruz";
  user.edad = 19;


  user.IniciarSesion();
  user.hacerReporte();
  user.cerrarSesion();
}
